"""
https://github.com/getnikola/nikola/blob/master/nikola/plugins/compile/rest/post_list.py
https://github.com/getnikola/nikola/blob/master/nikola/plugins/shortcode/post_list.py
"""
import os

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from nikola import utils
from nikola.plugin_categories import RestExtension


class Plugin(RestExtension):
    """Plugin for reST post-list directive."""

    name = "list_siblings"

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        directives.register_directive('list_siblings', SiblingListDirective)
        # self.site.register_shortcode('media', _gen_media_embed)
        SiblingListDirective.site = site
        return super(Plugin, self).set_site(site)


class SiblingListDirective(Directive):
    """Provide a reStructuredText directive to create a list of posts."""

    option_spec = {'base_folder': str}

    def run(self):
        """Run post-list directive."""
        # TODO: get base folder somehow automatically
        base_folder = self.options['base_folder']
        # filename = self.state.document.settings._nikola_source_path
        pages = [p for p in self.site.pages if not p.use_in_feeds and not p.is_private]
        pages = [p for p in pages if base_folder in p.folder]
        names = [p.source_link() for p in pages]
        names = [name.replace('/index.rst', '')[1:] for name in names]


        # Sort pairs
        # TODO: preserve some order if required
        names, pages = zip(*sorted(zip(names, pages)))

        # sort pages tree like
        def group_pages(pages, names, base_folder):
            result = []
            for page, name in zip(pages, names):
                if base_folder == os.path.dirname(name):
                    result.append({
                        'page': page,
                        'siblings': group_pages(
                            pages=[p for p in pages if name in p.folder],
                            names=[n for n in names if name in n],
                            base_folder=name
                        )
                    })
            return result
        groupped_pages = group_pages(pages, names, base_folder)
        if not group_pages:
            return []

        # register state and dependencies
        template = 'sibling_list_directive.tmpl'
        template_deps = self.site.template_system.template_deps(template)
        if self.state:
            # Register template as a dependency (Issue #2391)
            for d in template_deps:
                self.state.document.settings.record_dependencies.add(d)
        self.state.document.settings.record_dependencies.add(
            "####MAGIC####TIMELINE")

        # render list of links
        template_data = {
            'lang': utils.LocaleBorg().current_lang,
            'posts': groupped_pages,
            # Need to provide str, not TranslatableSetting (Issue #2104)
            'messages': self.site.MESSAGES,
            '_link': self.site.link,
        }
        output = self.site.template_system.render_template(
            template, None, template_data)

        if output:
            return [nodes.raw('', output, format='html')]
        else:
            return []
