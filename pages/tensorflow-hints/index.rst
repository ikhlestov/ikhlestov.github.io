.. title: Tensorflow Hints
.. slug: tensorflow-hints
.. date: 2016-11-02 14:41:13 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents:

Add logs to Summary Writer outside from graph
=============================================

Usual we use summary writer in such way:

.. code-block:: python

    # inside graph definition
    tf.scalar_summary("some_var", some_var)

    # inside graph execution
    with tf.Session() as sess:
        summary_writer = tf.train.SummaryWriter('logs_dir')
        merged_summary = tf.merge_all_summaries()
        # get results from session execution

        summary = tf.session.run(merged_summary)
        summary_writer.add_summary(summary, some_step)

As you can see you can get only variables from the graph. But what if we want some post 
processing(for example mean loss per epoch, not per batch) of just add some self generated
data? In this case we may generate `summary` by hands.

.. code-block:: python

    # no any definitions inside graph or session fetches.
    with tf.Session() as sess:
        summary_writer = tf.train.SummaryWriter('logs_dir')
        summary = tf.Summary(value=[
            tf.Summary.Value(tag="some_tag", simple_value=some_value),
            tf.Summary.Value(tag="mean_loss", simple_value=mean_loss)
        ])
        summary_writer.add_summary(summary, some_step)


Handle Memory Consumption by Graph
==================================

During training graphs on GPUs you may note that graph take all available free memory.
But what in case you have very simple model and just want to run 2 or 3 of the on GPU?
For such case you may use config inside session, that will provide to the model only required amount of memory.
More about this you may read in 
`tensorflow official docs <https://www.tensorflow.org/versions/master/how_tos/using_gpu/index.html#allowing-gpu-memory-growth>`__.

.. code-block:: python

    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    session = tf.Session(config=config, ...)

Dynamic vs. Static RNNs
=======================

Just forget about static RNNs, use Dynamic for your purposes.
They are faster to build and also not required manual resizing/spliting of the input data.
Full explanation why is it so you may found 
`here <http://www.wildml.com/2016/08/rnns-in-tensorflow-a-practical-guide-and-undocumented-features/>`__.

.. code-block:: python

    inputs = tf.placeholder(tf.int32, shape=[batch_size, num_steps])

    # usual RNN
    inputs_splited = [tf.squeeze(input_step, [1])
                      for input_step in tf.split(1, num_steps, inputs)]
    outputs, state = tf.nn.rnn(
        cell,
        inputs_splited,
        dtype=tf.float64)

    # for dynamic RNN we not required reshaping
    outputs, state = tf.nn.dynamic_rnn(
        cell,
        inputs,
        dtype=tf.float64)
    # if we provide data with shape num_step x batch_size
    # we can just provide time_major=True flag to dynamic RNN call
    inputs_transposed = tf.transpose(inputs, [1, 0])
    outputs, state = tf.nn.dynamic_rnn(
        cell,
        inputs_transposes,
        dtype=tf.float64,
        time_major=True)

Handle last state from RNN inside graph
=======================================

pass

Data Readers simple explanation
===============================

pass

tf.py_func inside data readers
==============================

pass

Variables and Placeholders dynamic shapes inside graph
======================================================

pass

