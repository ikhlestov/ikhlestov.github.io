.. title: Bash usage examples
.. slug: bash-usage-examples
.. date: 2019-01-07 20:52:54 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents


Navigating around
==================

.. code-block:: bash
    
    # list sizes of files
    $ ls -lah
    # colored
    $ ls -G
    # count quantity of files inside folder
    $ ls -1 | wc -l

Sizes

.. code-block:: bash

    # check free disk space
    $ df -h
    # get folder size
    $ du -hs
    # get folders size inside another one
    $ du -h --max-depth=1 some_folder

Search

.. code-block:: bash
    
    # search recursive by folders
    $ grep -r "/api/Profile/active_home_devices" static/
    # search by file content
    $ grep -R 'GCModel' SemanticProcessor/
    # find by filename
    $ find ~ -name readme.txt

Zipping/unzipping

.. code-block:: bash
    
    # unzip tar.gz file
    $ tar -xvzf filename.tar.gz
    # zip something
    $ zip archive_name source_name
    # unzip something
    $ unzip archive_name


Files routines
===============

Display part of the file

.. code-block:: bash
    
    $ cat filename | less
    $ tail -200 filename
    $ head -200 filename
    $ head -n 1000 filename | tail
    # display to stdout
    $ echo SOMETHING

Merge all files in folder to one

.. code-block:: bash

    $ cat folder_path/* > new_file


Copy content of some text file

.. code-block:: bash

    $ cat file_path | xclip -sel clip  # ubuntu
    $ pbcopy < file_path  # mac

Encoding:

.. code-block:: bash
    
    # get encoding of document
    $ enca filename
    # change encoding of doc
    $ enconv filename


Network routines
=================

Create an ssh key

.. code-block:: bash
    
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/key_name
    cat ~/.ssh/key_name.pub | xclip -sel clip  # ubuntu
    pbcopy < ~/.ssh/id_rsa.pub  # mac


Get list of all listened ports

.. code-block:: bash

    $ sudo netstat -peanut



One-liners
==========

Show running process by name with headers

.. code-block:: bash
    
    $ ps aux | egrep "required_name|PID"

Execute output of some command(assume it in text file)

.. code-block:: bash

    $ $(cat filename)

Check memory every 1 second

.. code-block:: bash
    
    $ watch -n 1 free -m

Get the location of the executable link

.. code-block:: bash
    
    $ readlink -f /usr/bin/java

Get dependencies

.. code-block:: bash
    
    $ readelf -d some_exe

Find location of installed files

.. code-block:: bash

    $ dpkg --listfiles libqt4-dev

Get CUDA version

.. code-block:: bash

    $ dpkg -l | grep cuda

Remove range of folders starts with numbers

.. code-block:: bash

    $ rm -r output/logs/{17..26}*

Send stdout to file and display it to the bash at the same time

.. code-block:: bash

    $ ./some_file.sh | tee -a logs.txt

Handle docker containers

.. code-block:: bash
    
    # all runing| second line| container name    | stop container by name
    $ docker ps | sed -n 2p  | awk '{print $NF}' | xargs docker stop
    # stop all running containers
    $ docker ps | awk '{print $NF}' | tail -n +2 | xargs docker stop

Rename some folders by pattern

.. code-block:: bash
    
    # find required folders  | split folder by '/' or '_' |
    # based on split generate new name | call `mv` command with `system ()` flag
    # note that splaces added in quotes
    $ find . -type d -name "celeb*" |  awk -F '/|_' '{system ("mv " $0 " " $2"_mobile_"$3)}'
