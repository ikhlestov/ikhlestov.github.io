.. title: Bash commans
.. slug: bash-commands
.. date: 2016-11-11 11:55:53 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents

- `one page bash tutorial <https://github.com/jlevy/the-art-of-command-line/blob/master/README.md>`__ `(ru) <https://github.com/jlevy/the-art-of-command-line/blob/master/README-ru.md>`__
- `bash command explanation(explain shell) <https://explainshell.com/>`__

Commands descriptions
=====================

- **``ls [options] [path]``** - list directory contents
 
  - ``ls -lahF`` - long format, all files, human readable format, files indicators

- **``file [path]``** - determine file type

- **``man <command name>``** - access to manual pages
  
  - ``man -k <search term>`` - find required search term in man pages
  - press ``/`` to start search inside man page and ``n`` to search next result

-   Files manipulations
    
    - **``mkdir [options] <directory>``** - make directories
      
      - ``mkdir -p`` - create parent directories
      - ``mkdir -v`` - verbose output

    - **``rmdir [options] <directory>``** - remove empty directories. Flags similar to ``mkdir`` 

    - **``touch [options] <filename>``** - change file timestamp. Can be used to create blank file.

    - **``cp [options] <source> <destination>``** - copy file or directory

      - ``cp -r <source> <destination>`` - copy some folder
      - ``cp -n ...`` - do not overwrite existing file

    - **``mv [options] <source> <destination>``** - move a file or directory

    - **``rm [options] <file>``** - remove vile or directory

      - ``rm -r <directory>`` - remove non empty directory
      - ``rm -i <file>`` - interactive mode
      - ``rm -d <path>`` - remove empty directories

Piping
======

TODO

bash[rc, _profile] explanation
==============================

TODO

bash scripting
==============

TODO

By category
===========

Create ssh key
----------------

.. code-block:: bash
    
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/key_name
    cat ~/.ssh/key_name.pub | xclip -sel clip

Tmux simple example
==================================================

When you close ssh session, scripts that were called from ssh user may be closed. To handle this situation you may run scripts under the sudo. Or use tmux. What we should do:

- Connect to VPN, required server ``ssh username@host_ip``
- Install tmux - ``sudo apt-get install tmux``
- Open new tmux session ``tmux new -s session_name``
- Run desired script.
- Detach session with hotkey ``ctrl+b ++ d`` (Means press ``ctrl + b`` first and after the ``d``)
- You may reconnect at this point to the server
- List all tmux session ``tmux ls``
- Connect to chosen session with ``tmux a -t session_name``
- Kill session from itself if not required any more ``ctrl+b ++ x``

Additional notes:

- In case of mouse scrolling not works - inside tmux type ``tmux set-option -g mouse on``
- If you want to be sure that tmux session will not be stopped - you may open new window under the sudo ``sudo tmux new -s window_name`` and after inside change the user ``su - username``
- Here exist quite full `cheat sheet for tmux <https://gist.github.com/MohamedAlaa/2961058>`__
- Copy from tmux screen can be some way inconvinient - so it's better to store output in some file: ``./script_name | tee -a logs.txt``
- In case you want to copy something - you may just highlight by mouse required region, and to past press ``ctrl+b ++ ]``

Tmux is very powerful tool with many other capabilities. For example you may work in one session with your team.

Another hints
=============


.. listing:: ubuntu-bash-hints.sh bash
