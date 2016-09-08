.. title: Python Tips
.. slug: python-tips
.. date: 2016-09-08 00:33:51 UTC
.. tags: python, tips
.. category: 
.. link: 
.. description: Some tips about python
.. type: text
.. author: Illarion Khlestov

exit from ipdb(for example in case of loop)

.. code-block:: python
    
    import os; os.system('kill -9 %d' % os.getpid())

also you may place such alias in ``.pdbrc`` file at home or project folder

.. code-block:: python
    
    import os

    alias kk os.system('kill -9 %d' % os.getpid())

or just jump to some line ``j 22``




