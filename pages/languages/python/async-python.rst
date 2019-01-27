.. title: Async Python
.. slug: async-python
.. date: 2018-04-30 09:47:30 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents

Asyncio
=======

General thoughts:

- Every task should be awaited somewhere so you've got an exception
- Don't use features directly
- Use `Executors <https://docs.python.org/3/library/concurrent.futures.html>`__ for the long term tasks(for example - some calculations)
- don't use ``__del__`` method for the resources cleanup. Use async metethod, for example ``await obj.close()`` or context manager ``async with obj:``
- to replace event loop it's better to change default loop fabric at the asyncio

Top-level functions:

- ``run()``
- ``create_task()``
- ``current_task()``
- ``all_tasks()``
- ``get_running_loop()``

async ``__init__`` method(factory)
----------------------------------

.. code-block:: python3

    class A:
    def __init__(self):
        self.data = None

    @classmethod
    async def create(cls):
        self = cls()
        self.data = await fetch(url)

    a = await A.create()

Shielded execution
------------------

It should be used in case task should be finished in any case, even with closed connection

.. code-block:: python3

    async def handler(request):
        await asyncio.shield(request.config['db'].execute("UPDATE ..."))
        return web.Response(text="OK")

Or you may use `aiojobs library <https://github.com/aio-libs/aiojobs>`__

Context variables
-----------------

Should be used for some small tasks as logging, tracing, etc.

.. code-block:: python3

    import contextvars
    var = contextvars.ContextVar('var', 'default')

    async def inner():
        log.debug("User name: %s", var.get())

    @routes.get('/{name}')
    async def handler(request):
        assert var.get() == 'default'
        var.set(request.match_info['name'])
        await inner()



Generators
=============================

``yield`` and ``yield from`` syntax
------------------------------------

Example of ``yield`` as generator:

.. code-block:: python3

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

.. code-block:: python3

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

.. code-block:: python3

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
--------------------------------------

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
