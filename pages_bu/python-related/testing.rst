.. title: Testing
.. slug: testing
.. date: 2017-12-06 16:40:34 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents

PyTest
======

.. code-block:: bash

    # Allow pdb/ipdb at the pytest
    pytest -s tests/

    # run pytest with coverage
    pytest --cov-report html --cov=. --cov-config coverage.config tests/

    # Run pytest coverage for many installed django apps at once
    py.test --cov-report html --cov={app1, app2, ...} */tests.py

Example **coverage.config** file
---------------------------------

.. code-block::

    [run]
    source = package_name
    omit = .venv/*
           tests/*
           setup.py
           */__init__.py

    [report]
    # Regexes for lines to exclude from consideration
    exclude_lines =
        # Have to re-enable the standard pragma
        pragma: no cover
        # Don't complain if non-runnable code isn't run:
        if 0:
        if __name__ == .__main__.:

**--runslow** flag
-------------------

.. code-block:: python3

    import pytest

    def pytest_addoption(parser):
        parser.addoption("--runslow", action="store_true",
                         default=False, help="run slow tests")


    def pytest_collection_modifyitems(config, items):
        if config.getoption("--runslow"):
            # --runslow given in cli: do not skip slow tests
            return
        skip_slow = pytest.mark.skip(reason="need --runslow option to run")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)

Mocks
=====

Imports order matters
---------------------

.. code-block:: python3

    from unittest.mock import patch

    # if you use
    import some.class_name

    # in this case you should use mock as
    with patch('some.class_name') as mock:
        pass

    # but if you import with 'from' to the package 'package_name'
    from some import class_name

    # you should mock with
    with patch('package_name.class_name') as mock:
       pass


Decorators orders
-----------------

If we use mocks as decorators with some features we should preserve such order

.. code-block:: python3

    from unittest.mock import patch
    import pytest

    @pytest.fixture
    def my_fixture():
        return
    
    @patch('some.library.second_patch')
    @patch('some.library.first_patch')
    def test_protocol_prepare(first_patch, second_patch, my_fixture):
        assert True


Patching many instances
-----------------------

Sometimes you need to patch a lot of instances. In this case you can use ``patch.multiple``:

At some ``script.py``

.. code-block:: python3

    A = 1
    B = 2

At tests:

.. code-block:: python3

    with patch.multiple('script', A=DEFAULT, B=DEFAULT) as patches_dict:
        a_patch = patches_dict['A']
        b_patch = patches_dict['B']

In case you want this in fixture, you may use such approach:

.. code-block:: python3

    from unittest.mock import patch
    import pytest

    @pytest.fixture
    def multy_patch():
        patcher = patch.multiple('module', var_1=DEFAULT, var_2=DEFAULT)
        started_patcher = patcher.start()
        yield started_patcher
        patcher.stop()

    def test_something(multy_patch):
        var_1_patch = multy_patch['var_1']


Classes patching
----------------

If you want to patch some method of the tested class itself, use ``patch.object``:

.. code-block:: python3

    from unittest.mock import patch, PropertyMock

    class ClassName:

        def method_name(self):
            pass

        def __hidden_method(self):
            pass

        @property
        def my_property(self):
            pass
    
    # in case of usual method
    with patch.object(ClassName, 'method_name') as mock:
        mock.assert_called_with(key=key)

    # in case of hidden __method_name
    with patch.object(ClassName, '_ClassName__hidden_method') as mock:
        mock.assert_called()

    # for properties
    with patch('ClassName.my_property', new_callable=PropertyMock) as property_mock:
        property_mock.return_value = 42
        myclass = MyClass()
        mock_last_transaction.assert_called_once_with()

In case you want patch ``__init__`` method and some another method

.. code-block:: python3

    from unittest.mock import patch

    class ClassName:

        def __init__(self, *args, **kwargs):
            # some complicated init
            pass

        def some_important_method(self):
            pass

    # first solution without context manager
    patcher = patch('module.name.ClassName')
    MockedClass = patcher.start()
    isntance = MockedClass()
    instance.some_important_method.return_value = "your desired value"

    # with context managers
    with patch('module.name.ClassName') as MockedClass:
        instance = MockedClass.return_value
        instance.some_important_method.return_value = "your desired value"


Interactions with mocks
-----------------------

.. code-block:: python3

    mock.assert_called()
    mock.assert_called_once_with()
    mock.assert_called_with(key=key)
    assert mock.call_count == 1

Async testing
-------------

pytest-asyncio
~~~~~~~~~~~~~~~~~~

In case you want make ``await`` calls inside your tests you may use `pytest-asyncio <https://pypi.org/project/pytest-asyncio/>`__

For example you have such code that should be tested

.. code-block:: python3

    async def my_method():
        pass

By default you may test it as

.. code-block:: python3

    import asyncio

    def test_my_method():
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(my_method())

But you may replace it with

.. code-block:: python3

    import pytest

    @pytest.mark.asyncio
    async def test_my_method():
        result = await my_method()

asynctest
~~~~~~~~~~~~~

When you want to mock some objects that should be awaitable you may use `asynctest <http://asynctest.readthedocs.io/en/latest/index.html>`__

.. code-block:: python3

    class SomeClass:
        def __init__(self, lib):
            self.lib = lib

        async def some_call(self):
            await self.lib()

    # just use another imports
    from asynctest import CoroutineMock, patch

    def test_some_class():
        lib = CoroutineMock()
        cls_ = SomeClass(lib)
        asyncio.get_event_loop().run_until_complete(cls_.some_call())

Hypothesis Testing
==================

Sometimes you may want to test hypothesis. For this you may use such libraries:

- `Hypothesis <https://hypothesis.readthedocs.io/en/latest/index.html>`__ python package
- `TLA+ <https://lamport.azurewebsites.net/tla/tla.html>`__
- `Alloy <https://en.wikipedia.org/wiki/Alloy_(specification_language)>`__
