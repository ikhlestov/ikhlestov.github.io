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


List/Tuples(iterators)
======================

Comprehensions
--------------

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


Using * to grab excess items
----------------------------

.. code-block:: python

    a, b, *rest = range(5)
    a, b, rest
    # out: (0, 1, [2, 3, 4])

    a, b, *rest = range(2)
    # out: (0, 1, [])

    # can be assigned at any position
    a, *body, c, d = range(5)
    a, body, c, d
    # out: (0, [1, 2], 3, 4)

Nested tuple unpacking
----------------------

.. code-block:: python
    
    # if we have list of tuples like this
    metro_areas = [ ('Tokyo','JP',36.933,(35.689722,139.691667)), '...' ]
    # we can unpack it like this:
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:
            print("Do something")

Namedtuples
-------------------

Intro
~~~~~

.. code-block:: python

    from collections import namedtuple
    City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
    # or provide just space delimited string
    City = namedtuple('City', 'name country population coordinates')

    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

    City._fields
    # out: ('name', 'country', 'population', 'coordinates')

    # convert namedtuple to dict
    tokyo._asdict()

Inherit from namedtuple
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: pycon
    
    >>> Car = namedtuple('Car', 'color mileage')
    >>> class MyCarWithMethods(Car):
    ...     def hexcolor(self):
    ...         if self.color == 'red':
    ...            return '#ff0000'
    ...         else:
    ...             return '#000000'

    >>> c = MyCarWithMethods('red', 1234)
    >>> c.hexcolor()
    '#ff0000'

Use _fields attribute
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: pycon
    
    >>> Car = namedtuple('Car', 'color mileage')
    >>> ElectricCar = namedtuple(
    ...     'ElectricCar', Car._fields + ('charge',))

Additional methods
~~~~~~~~~~~~~~~~~~

.. code-block:: pycon

    >>> my_car._asdict()
    OrderedDict([('color', 'red'), ('mileage', 3812.4)])
    >>> json.dumps(my_car._asdict())
    '{"color": "red", "mileage": 3812.4}'

    >>> my_car._replace(color='blue')
    Car(color='blue', mileage=3812.4)

    >>> Car._make(['red', 999])
    Car(color='red', mileage=999)

Pickle and unpickle namedtuples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def isnamedtupleinstance(x):
        t = type(x)
        b = t.__bases__
        if len(b) != 1 or b[0] != tuple:
            return False
        f = getattr(t, '_fields', None)
        if not isinstance(f, tuple):
            return False
        return all(type(n) == str for n in f)

    def pickle_namedtuple(instance):
        data = instance._asdict()
        for key, value in data.items():
            if isnamedtupleinstance(value):
                data[key] = pickle_namedtuple(value)
        dump = {
            "namedtuple": True,
            "class_name": instance.__class__.__name__,
            "fields": instance._fields,
            "data": data
        }
        return dump
        
    def restore_namedtuple(dump):
        class_ = namedtuple(dump["class_name"], dump["fields"])
        restored_data = {}
        for field_name, field_data in dump["data"].items():
            if isinstance(field_data, dict) and field_data.get("namedtuple"):
                field_data = restore_namedtuple(field_data)
            restored_data[field_name] = field_data
        return class_(**restored_data)

Slicing
--------

Slices can be assigned to variable and used after assigning:

.. code-block:: pycon
    
    >>> test = 'test string'
    >>> test[0:4]
    'test'
    >>> first_slice = slice(0, 4)
    >>> test[first_slice]
    'test'
    >>> second_slice = slice(4, None)
    >>> test[second_slice]
    ' string'

Assigning to slices
-------------------

.. code-block:: pycon

    >>> l = list(range(10))
    >>> l
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
    >>> l[2:5] = [20, 30]
    >>> l
    [0, 1, 20, 30, 5, 6, 7, 8, 9]
    >>> del l[5:7]
    >>> l
    [0, 1, 20, 30, 5, 8, 9]

bisect module
-------------

Return the corresponding letter grade

.. code-block:: pycon

    >>> def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    ...     # returns index of where score should be inserted
    ...     i = bisect.bisect(breakpoints, score)
    ...     return grades[i]
    ...
    >>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    ['F', 'A', 'C', 'C', 'B', 'A', 'A']

Things in Python3
=================

Get first and last line of the file
-----------------------------------

.. code-block:: pycon

    >>> with open("using_python_to_profit") as f:
    ...     first, *_, last = f.readlines()
    >>> first
    'Step 1: Use Python 3\n'
    >>> last
    'Step 10: Profit!\n'

Keyword only arguments
----------------------

.. code-block:: python

    def f(a, b, *args, option=True):
        pass

Raise chained exceptions
------------------------

.. code-block:: python

    raise exception from e

Context Managers
================

Class based
-----------

.. code-block:: python

    class CustomOpen(object):
        def __init__(self, filename):
            self.file = open(filename)

        def __enter__(self):
            return self.file

        def __exit__(self, ctx_type, ctx_value, ctx_traceback):
            self.file.close()

    with CustomOpen('file') as f:
        contents = f.read()

contextlib based
-----------------

.. code-block:: python

    from contextlib import contextmanager

    @contextmanager
    def custom_open(filename):
        f = open(filename)
        try:
            yield f
        finally:
            f.close()

    with custom_open('file') as f:
        contents = f.read()

Errors suppressing
------------------

.. code-block:: python

    import contextlib

    with contextlib.suppress(FileNotFoundError):
        os.remove('somefile.tmp')


Working with images
===================

While working with images you should be careful with order in returned values.

.. code-block:: python

    # in general in any case reading an image will return it as `height x width x channels`
    from cv2 import imread as cv_imread
    from cv2 import resize as cv_resize
    from skimage.io import imread as sk_imread
    from skimage.transform import resize as sk_resize
    from PIL.Image import open as pil_imread
    from matplotlib.pyplot import imread as plt_imread
    import numpy as np

    # assume we have some image with height == 687 and width == 409
    print(cv_imread(image_path).shape)
    print(sk_imread(image_path).shape)
    print(np.asarray(pil_imread(image_path)).shape)
    print(plt_imread(image_path).shape)
    height, width, ch = image.shape

    # (687, 409, 3)
    # (687, 409, 3)
    # (687, 409, 3)
    # (687, 409, 3)

    # on the hand resizer may get arguments in different order
    # width-first
    cv_resize(image, (new_width, new_height))
    np.asarray(pil_image.resize((new_width, new_height)))

    # height first
    sk_resize(image, (new_height, new_width))

Miscellaneous
=============

.. listing:: python-hints.py python
