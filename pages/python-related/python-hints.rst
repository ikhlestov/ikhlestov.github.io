.. title: Python Hints
.. slug: python-hints
.. date: 2017-03-21 16:21:33 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents

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

Checking args prior to runtime
==============================

It is useful to check args received by function prior to runtime.
This can be implemented with decorator:

.. code-block:: python
    
    # define decorator
    def check_args(*types):
        def real_decorator(func):
            def wrapper(*args, **kwargs):
                for val, typ in zip(args, types):
                    if not isinstance(val, typ):
                        msg = "Value {} is not of expected type {}".format(val, typ)
                        raise ValueError(msg)
                return func(*args, **kwargs)
            return wrapper
        return real_decorator

    # example usage of decorator
    @check_args(str, int)
    def print_something(name, quantity):
        print("name: {}, quantity: {}".format(name, quantity))


Palindromes
===========

.. code-block:: python
    
    # simple example
    def is_palindrome(s):
        return s == s[::-1]

    # for unicode data
    import unicodedata
    def is_palindrome(s):
        if any(unicodedata.combining(c) for c in s):
            s = unicodedata.normalize('NFC', s)
        return s == s[::-1] 

Change handling function based on length of provided arguments
==============================================================

.. code-block:: python

    import math
    ​
    formula_gerona = "%.5f*(%.5f-a)*(%.5f-b)*(%.5f-c)"
    figur = [
        lambda d: math.pi*((d/2.0)**2),                                  #Circle
        lambda a,b: a*b,                                                 #Square/Rectangle
        lambda a,b,c: math.sqrt(eval(formula_gerona%(((a+b+c)/2,)*4) )), #Triangle
    ]
    ​
    def simple_areas(*args):
        return figur[len(args)-1](*args)

PyTest
======

.. code-block:: bash

    # Allow pdb/ipdb at the pytest
    pytest -s tests/

    # run pytest with coverage
    coverage run -m pytest tests

    # Run pytest coverage for many installed django apps at once
    py.test --cov-report html --cov={app1, app2, ...} */tests.py

Example .coveragerc file:

.. code-block::

    [run]
    source = package_name
    omit = site-packages, .env

    [html]
    directory = htmlcov

String formatting
=================

.. code-block:: python
    
    # dictionary string formatting
    params = {"uid":"sa", "pwd":"secret"}
    print("%(pwd)s" % params)
    print("{pwd}".format(**params))
    # out: 'secret'

    # strip float precision length
    print('%.2f' % 0.1245125)
    print('{:.2f}'.format(0.1245125))
    # out: 0.12

    # free space before word
    print('%10s' % 'some')
    print('{:>10}'.format('some'))
    # out: '        some'
    print('%-10s' % 'some')
    print('{:<10}'.format('some'))
    # out: 'some        '

Comprehensions
==============

.. code-block:: python
    
    # nested list comprehension
    mylist = [['10', '20', '30'], ['1', '2', '3']]
    # flattened list
    new_list = [float(entry) for sublist in mylist for entry in sublist]
    [10.0, 20.0, 30.0, 1.0, 2.0, 3.0]
    # nested list of floats
    new_list = [[float(entry) for entry in sublist] for sublist in mylist]
    [[10.0, 20.0, 30.0], [1.0, 2.0, 3.0]]
    # also can be used to generate cartesian product
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors
                             for size in sizes]
    [('black', 'S'),
     ('black', 'M'),
     ('black', 'L'),
     ('white', 'S'),
     ('white', 'M'),
     ('white', 'L')]
     # the same as:
     for color in colors:
        for size in sizes:
            print(color, size)

    # dict comprehension
    my_dict = {key:value for item in list if conditional}

Generators, yield from syntax
=============================

Example of ``yield`` as generator:

.. code-block:: python

    def generator(x):
        # here generator will be interupted and wait for next call
        yield x
        yield x*2

    # example:
    gen = generator(10)
    next(gen)
    # out: 10
    next(gen)
    # out: 20

Example of ``yield`` as coroutine:

.. code-block:: python

    def writer():
        while True:
            # rcv a data
            w = yield
            print("was received:", w)

    w = writer()
    # initialize the generator
    w.send(None)
    w.send(10)
    # out: "was received: 10"
    w.send("some text")
    # out: "was received: some text"

Example usage of ``yield from`` syntax:

.. code-block:: python

    # define our generator
    def generator():
        for i in range(4):
            yield i

    # manually fetch data
    def fetcher(g):
        for fetch in g:
            yield fetch

    # yield from fetcher
    def fetcher_yield(g):
        yield from g

    # examples:
    fetch_results = fetcher(generator())
    for i in fetch_results:
        print(i)

    fetch_results = fetcher_yield(generator())
    for i in fetch_results:
        print(i)


Change existing object with generator
=====================================

It is possible to create object at generator and after only change it's value.
This will reduce memory consumption, but can lead to some errors:

.. code-block:: python
    
    def generator():
        d = {}
        yield d
        counter = 0
        while True:
            d["value"] = counter
            counter += 1
            yield

    gen = generator()
    res = next(gen)
    print(res)
    # out: {}
    
    # modify same dict
    next(gen)
    print(res)
    # out: {'value': 0}


Miscellaneous
=============

.. listing:: python-hints.py python

.. listing:: python-hints.sh bash
