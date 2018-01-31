.. title: Git notes
.. slug: git-notes
.. date: 2016-06-26 01:03:23 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

Cool resourses:

- `Git cheat sheet <http://files.zeroturnaround.com/pdf/zt_git_cheat_sheet.pdf>`__
- `Another cheat sheet <https://gist.github.com/eashish93/3eca6a90fef1ea6e586b7ec211ff72a5>`__
- `Undoing things <https://www.git-tower.com/learn/git/ebook/en/command-line/advanced-topics/undoing-things>`__

**Installing git repo with pip**

.. code-block::

    pip install -e \
    git+ssh://git@github.com/username/repository@[branch|tag|commit]#egg=common[&subdirectory=dir_name]

.. listing:: git.sh bash
