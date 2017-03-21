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
    # out: 'secret'

Comprehensions
==============

.. code-block:: python
    
    # nested list comprehension
    mylist = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20']]
    # flattened list
    new_list = [float(entry) for sublist in mylist for entry in sublist]
    # nested list of floats
    new_list = [[float(entry) for entry in sublist] for sublist in mylist]

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


Miscellaneous
=============

.. listing:: python-hints.py python

.. listing:: python-hints.sh bash
