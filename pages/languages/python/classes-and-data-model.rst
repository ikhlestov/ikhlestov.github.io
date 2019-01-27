.. title: Classes and Data Model
.. slug: classes-and-data-model
.. date: 2018-04-30 10:00:48 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents

More about Python Data Model you may read in the `official documentation <https://docs.python.org/3/reference/datamodel.html>`__

Using namespace classes
=======================

This classes allow you directly assign params to class

.. code-block:: python

    from types import SimpleNamespace
    class S(SimpleNamespace):
        pass

    s = S(some='some', value='42')
    print(s.some)
    # out: 'some'
    print(s.value)
    # out: '42'

can be replaced such way:

.. code-block:: python

    class adict(dict):
        def __init__(self, *av, **kav):
            dict.__init__(self, *av, **kav)
            self.__dict__ = self

Slots Usage
===========

.. code-block:: pycon

    >>> class Point:
    ...     __slots__ = ('x', 'y')
    ...
    >>> p = Point()
    >>> p.x = 1
    >>> p.y = 2
    >>> p.z = 33
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Point' object has no attribute 'z'

TODO: add singleton, metaclasses examples
