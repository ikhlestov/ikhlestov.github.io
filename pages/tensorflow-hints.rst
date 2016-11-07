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

When using rnn usual we get last state of RNNs and send back the through feed dict:

.. code-block:: python

    # inside model definition
    cell = tf.nn.rnn_cell.LSTMCell(num_units=n_hidden)
    self.initial_state = cell.zero_state(batch_size, dtype=tf.float32)
    rnn_out, self.last_state_fw = nn.dynamic_rnn(
        cell=cell,
        inputs=inputs,
        initial_state=self.initial_state)

    # and after during session
    last_state = None
    if last_state is not None:
        feed_dict = {self.initial_state: last_state}
    _, last_state = sess.run(
        [self.learning_op, self.last_state],
        feed_dict=feed_dict)

But in this case we move last state from GPU memory and backwards. This is unreasonable.
We can handle last state inside GPU directly as:

.. code-block:: python

    # inside model definition
    last_state = tf.Variable(tf.zeros([batch_size, n_hidden]), trainable=False)
    cell = tf.nn.rnn_cell.LSTMCell(num_units=n_hidden)
    rnn_out, final_states = tf.nn.dynamic_rnn(
        cell=cell,
        inputs=inputs,
        initial_state=last_state)
    
    # and after to assign new value to last state we should use small trick
    with tf.control_dependencies([tf.assign(last_state, final_states)]):
        rnn_out = tf.identity(rnn_out)

Run model without GPU
=====================
In case you have GPUs on your machine but want to train without them, you should
just pass additional env variable `CUDA_VISIBLE_DEVICES=''` during script call.

.. code-block:: bash

    $ CUDA_VISIBLE_DEVICES='' python some_model.py
    

Data Readers simple explanation
===============================

pass

tf.py_func inside data readers
==============================

pass

Variables and Placeholders dynamic shapes inside graph
======================================================

pass

