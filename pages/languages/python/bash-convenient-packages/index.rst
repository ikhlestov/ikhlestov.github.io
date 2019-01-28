.. title: Python bash libraries
.. slug: bash-convenient-packages
.. date: 2017-03-21 16:21:33 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents


ntfy
==============

Brings notification to your shell.
`PyPi <https://pypi.python.org/pypi/ntfy>`__         
`Docs <http://ntfy.readthedocs.io/en/latest/>`__

.. code-block:: bash

    $ ntfy send message
    $ ntfy send 'test long message'
    # send message after command completion
    $ ntfy send sleep 10
    $ ntfy send cat some.txt

Cand be replaced by ubuntu `notify-send <http://manpages.ubuntu.com/manpages/trusty/man1/notify-send.1.html>`__

.. code-block:: bash

    $ notify-send <title> <message> 




http.server
===========

.. code-block:: shell

    # python2
    python -m SimpleHTTPServer

    # python3
    python3 -m http.server


json pretty printing
====================

.. code-block:: bash

    $ echo '{"json":"obj"}' | python -m json.tool

    {
        "json": "obj"
    }


pip
====

.. code-block:: bash

    # unistall all existing packages
    pip freeze | xargs pip uninstall -y


Print system configuration
===========================

.. code-block:: bash

    $ python -m sysconfig
    # Platform: "macosx-10.6-intel"
    # Python version: "3.6"
    # Current installation scheme: "posix_prefix"


pycodestyle
===========

.. code-block:: bash

    pycodestyle ./project_name



virtual environment
===================

.. code-block:: bash

    # create new vierualenv with venv without pip
    python3.6 -m venv $ENV_NAME --without-pip
    source $ENV_NAME/bin/activate
    wget https://bootstrap.pypa.io/get-pip.py
    python get-pip.py
    
    # or with pip just
    python3.6 -m venv $ENV_NAME

    # with virtualenv
    virtualenv -p /usr/local/bin/python2.7 env_name



Working with archives
=====================

.. code-block:: bash

    # Create a new TAR archive
    $ python3 -m tarfile -c <tarname>.tgz <file> <file>

    # Extract from an existing TAR archive
    $ python3 -m tarfile -e <tarname>.tgz

    # pack directory into archive and make it executable
    $ python3 -m zipapp myapp
    $ python3 myapp.pyz
    # <output from myapp>
