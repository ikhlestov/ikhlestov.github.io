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

Mocks
=====

Imports order matters
---------------------

.. code-block:: python

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


Pathcing testing class itself
-----------------------------

If you want to patch some method of the tested class itself, use ``patch.object``:

.. code-block:: python
    
    # in case of usual method
    with patch.object(ClassName, 'method_name') as mock:
        mock.assert_called_with(key=key

    # in case of hidden __method_name
    with patch.object(ClassName, '_ClassName__method_name') as mock:
        mock.assert_called()

Patching many instances
-----------------------

Sometimes you need to patch a lot of instances. In this case you can use ``patch.multiple``:

.. code-block:: python

    # in script.py

    A = 1
    B = 2

    # in tests
    with patch.multiple('script', A=DEFAULT, B=DEFAULT) as patches_dict:
        a_patch = patches_dict['A']
        b_patch = patches_dict['B']

In case you want this in fixture, you may use such approach:

.. code-block:: python

    @pytest.fixture
    def multy_patch():
        patcher = patch.multiple('module', var_1=DEFAULT, var_2=DEFAULT)
        started_patcher = patcher.start()
        yield started_patcher
        patcher.stop()

    def test_something(multy_patch):
        var_1_patch = multy_patch['var_1']


Patching properties
-------------------

If you want to patch property, use such approach:

.. code-block:: python

    class MyClass:
    @property
    def last_transaction(self):
        # an expensive and complicated DB query here
        pass

    def test():
        with mock.patch('MyClass.last_transaction', new_callable=PropertyMock) as mock_last_transaction:
            mock_last_transaction.return_value = Transaction()
            myclass = MyClass()
            mock_last_transaction.assert_called_once_with()
