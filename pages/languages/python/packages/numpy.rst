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

If you want to make batches, where N+1 batch will follow N batch, try this:

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

Change display methods

.. code-block:: python

    np.set_printoptions(precision=2)
    np.set_printoptions(suppress=True)

Split some array in folds(numpy)

.. code-block:: python

    y_folds = np.array_split(y_digits, 3)

Shuffle the indices for test data

.. code-block:: python

    indexes = np.random.permutation(len(iris_X))

Select max value based on another array max value(numpy)

.. code-block:: python

    best_alpha = alphas[scores.index(max(scores))]

Reshape one array to another one shape

.. code-block:: python

    face_compressed.shape = face.shape

Reshape numpy array with dynamically calculated second dimension

.. code-block:: python

    test_data = np.zeros((4, 3))
    test_data.shape  # (4, 3)
    reshaped = test_data.reshape((6, -1))
    reshaped.shape  # (6, 2)

Create list of 3 random items form 0 to 255

.. code-block:: python

    np.random.randint(0, high=256, size=(3, )).tolist()

Assign values to one line in array(notes for tensorflow)
.. code-block:: python

    M_t = np.arange(15).reshape(5, 3)
    # array([[ 0,  1,  2],
    #        [ 3,  4,  5],
    #        [ 6,  7,  8],
    #        [ 9, 10, 11],
    #        [12, 13, 14]])
    indexes = np.array([0, 1, 0, 0, 0])
    new_value = np.arange([101, 102, 103])
    (M_t.T * (-1 * (indexes -1))).T + np.outer(indexes, new_value)
    # array([[  0,   1,   2],
    #        [103, 104, 105],
    #        [  6,   7,   8],
    #        [  9,  10,  11],
    #        [ 12,  13,  14]])
