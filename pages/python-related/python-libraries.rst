.. title: Python Libraries
.. slug: python-libraries
.. date: 2016-09-07 21:49:40 UTC
.. tags: python, libraries
.. category: 
.. link: 
.. description: Some useful libraries for python
.. type: text
.. author: Illarion Khlestov

.. contents:: List of libraries:


tqdm
====
Progress bar for any iterations.
`PyPi <https://pypi.python.org/pypi/tqdm>`__

.. code-block:: python

    import time
    from tqdm import tqdm

    for i in tqdm(range(10)):
        time.sleep(10)


pyperclip
==============
An easy python interface to the system clipboard.
`Pypi <https://github.com/asweigart/pyperclip>`__

.. code-block:: python
    
    import pyperclip as clip

    # copy string to buffer
    clip.copy("Some text")

    # copy text from buffer
    data = clip.paste()  

Note: you may also try `pyclip-copycat <https://pypi.python.org/pypi/pyclip-copycat/1.0>`__


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

sultan
======
Sultan is a Python package for interfacing with command-line utilities, like yum, apt-get, or ls, in a Pythonic manner.
`Git <https://github.com/aeroxis/sultan>`__

.. code-block:: python

    from sultan.api import Sultan
    s = Sultan()
    s.sudo("yum install -y tree").run()

in one line
===========

- `youtag <https://github.com/JoseTomasTocino/yotaq>`__ - Your Own Task Queue for Python
- `tenacity <https://github.com/jd/tenacity>`__ - Retrying library for Python
