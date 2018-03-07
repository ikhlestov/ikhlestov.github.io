.. title: Numpy
.. slug: numpy
.. date: 2016-10-12 23:12:43 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

`Cool brief questions about numpy <https://www.machinelearningplus.com/101-numpy-exercises-python/>`__

If you want create batches, where N+1 batch will follow N batch, try this:

.. code-block:: python

    import numpy as np

    batch_quantity = 3
    batch_size = 2
    some_embedding = 4

    initial_data = np.arange(24)
    reshaped = initial_data.reshape(batch_size, batch_quantity, some_embedding)
    result_data = reshaped.transpose(1, 0, 2)

    print(result_data)
    # [[[ 0  1  2  3]
    #   [12 13 14 15]]
    #
    #  [[ 4  5  6  7]
    #   [16 17 18 19]]
    #
    #  [[ 8  9 10 11]
    #   [20 21 22 23]]]

Another info notes:

.. listing:: numpy.py python
