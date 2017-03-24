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

Change inline setting during training
=====================================

.. code-block:: python

    x = some_tensor
    is_training = tf.placeholder(tf.bool, shape=[])
    # should define as function, because under condition should be callable
    def apply_dropout(): # Function to apply when training mode ON.
         return tf.nn.dropout(x, keep_prob)
    # Only apply dropout at training time.
    # tf.cond(cond, true_function, false_function)
    new_x = tf.cond(is_training, apply_dropout, lambda: x)


Get last output from rnn
========================

.. code-block:: python

    rnn_out, last_state = tf.nn.dynamic_rnn(..)
    rnn_out = tf.reverse(rnn_out, [False, True, False])
    rnn_out_last = tf.slice(rnn_out, [0, 0, 0], [-1, 1, -1])

Batch Normalization
===================
Notes based on `this paper <https://arxiv.org/pdf/1502.03167v3.pdf>`__. I think to understood BN enough just quickly pass through 3rd paragraph.
At glance batch normalizaion helps training as the layer does not have to learn offsets in the input data, and can focus on how to best combine features.

It seems that when BN is used, such nuances should be considered:

If we have usual layer as :math:`z = g(Wu + b)`,
where :math:`g(.)` is the nonlinearity such as sigmoid or ReLU
batch normalization should be applied as 
:math:`z = g(BN(Wu))`. Note that BN applied **before** nonlinearity.
Also due to internal shift :math:`\beta` existed in BN bias :math:`b` can be omitted.

If we apply `batch norm layer from tensorflow <https://www.tensorflow.org/api_docs/python/contrib.layers/higher_level_ops_for_building_neural_network_layers_#batch_norm>`__
we should clear declare param `is_training=True/False` during training/inference. Because for training and inference different approaches used by BN.
To understood what exactly each param handled by layer mean - take a look on algorithms 1 and 2 descriptions in the `original paper <https://arxiv.org/pdf/1502.03167v3.pdf>`__ on pages 3 and 4 accordingly. Really is seems that it's enough to use tf contrib layer with all default params only with redefined `scale` param. :math:`\gamma` (scale) and :math:`\beta` (shift) params will be trainable by default.

.. code-block:: python

    logits = tf.matmul(inputs, W)
    normed_logits = tf.contrib.layers.batch_norm(inputs, scale=True)
    output = tf.sigmoid(normed_logits)

    # next lines should be added so Optimizer can find variables to optimize
    update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
    if update_ops:
        updates = tf.group(*update_ops)
        total_loss = control_flow_ops.with_dependencies([updates], total_loss)

Maybe sometimes easier use *in place* update of alpha and beta. In docs was mentioned that this approach can be a little bit slower, but at least it less boilerplate. Also for training flag it may be conveniently to use tflearn train flags

.. code-block:: python
    
    is_training = tf.placeholder(tf.bool, shape=[])

    output = tf.contrib.layers.batch_norm(
        _input, scale=True, is_training=is_training,
        updates_collections=None)

Applying weights regularization
===============================
.. code-block:: python
    
    # some usual loss definition as cross-entropy or MSE
    initial_loss = cross_entropy
    l2_loss = tf.add_n(
        [tf.nn.l2_loss(var) for var in tf.trainable_variables()])

    optimizer = tf.train.SomeOptimizer(learning_rate)
    # now we should minimize sum of initial loss and regularization
    train_step = optimizer.minimize(cross_entropy + l2_loss * weight_decay)

Load part of graph from previous run
====================================
.. code-block:: python

    all_vars = tf.all_variables()
    restored_scopes = ['Scope_1', 'Scope_2']
    # get only restored variables
    restored_vars = [
        v for v in all_vars if v.name.split('/')[0] in restored_scopes]
    loader = tf.train.Saver(var_list=restored_vars)
    loader.restore(sess, previous_model_saves)

    # now initialize all not resotred variables
    initialized_vars = [v for v in all_vars if v not in restored_vars]
    sess.run(tf.variables_initializer(initialized_vars))

    # also sometimes to clarify it's better to print restored variables
    print("Such vars were be restored")
    for v in restored_vars:
        print(v.name)

Count trainable params
======================
.. code-block:: python
    
    total_parameters = 0
    for variable in tf.trainable_variables():
        shape = variable.get_shape()
        variable_parametes = 1
        for dim in shape:
            variable_parametes *= dim.value
        total_parameters += variable_parametes
    print("Total training params: %.5fM" % (total_parameters / 1e6))

Handle TensorArrays correct way inside tf.while_loop
====================================================

Sometimes we want to pass output from one loop step, to next step.
For this we can use ``tf.TensorArray`` with read and write operations.
But in case we read and write to same tensorarray inside loop - we should manually set number of available while loop ``parallel_iterations=1``.
This is because in case of parallel loop execution(parallel_iterations > 1) some thread may try to read info from tensorArray, that was not written to it by another one thread.
Try to copy/run code snippet below.

.. code-block:: python

    from tensorflow.examples.tutorials import mnist
    # code require tensorflow verions==1.0
    import tensorflow as tf

    batch_size = 30
    BREAK_CODE = True
    if BREAK_CODE:
        # fail with this settings
        parallel_iterations = 10
    else:
        # work as expected with this settings
        parallel_iterations = 1

    _input = tf.placeholder(tf.float32, [batch_size, 784])
    targets = tf.placeholder(tf.float32, [batch_size, 10])

    input_array = tf.TensorArray(dtype=tf.float32, size=batch_size + 1)
    output_array = tf.TensorArray(dtype=tf.float32, size=batch_size)
    one_image = _input[0, :]
    input_array = input_array.write(0, one_image)
    W = tf.get_variable('W', [784, 10],
                        tf.float32, tf.random_uniform_initializer())
    W_out = tf.get_variable("W_out", [10, 784],
                            tf.float32, tf.random_uniform_initializer())


    def body(i, inp_array, out_array):
        local_input = inp_array.read(i)
        local_input_reshaped = tf.reshape(local_input, [1, 784])
        result = tf.matmul(local_input_reshaped, W)
        out_array = out_array.write(i, result)
        next_input = tf.sigmoid(tf.squeeze(tf.matmul(result, W_out), axis=0))
        inp_array = inp_array.write(i + 1, next_input)
        return (i + 1, inp_array, out_array)


    def cond(i, *args):
        return i < batch_size

    _, _, output_array = tf.while_loop(
        cond, body, [0, input_array, output_array],
        parallel_iterations=parallel_iterations)
    results = output_array.stack()
    results = tf.reshape(results, [batch_size, 10])

    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
        logits=results, labels=targets))
    train_op = tf.train.AdamOptimizer().minimize(loss)

    if __name__ == '__main__':
        mnist_data = mnist.input_data.read_data_sets(
            "/tmp/MNIST_data/", one_hot=True)
        steps = 200
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            for i in range(steps):
                batch = mnist_data.train.next_batch(batch_size)
                feed_dict = {
                    _input: batch[0],
                    targets: batch[1]
                }
                fetches = [loss, train_op, results]
                res_loss, _, res = sess.run(fetches, feed_dict=feed_dict)


TODO
====

- Data Readers simple explanation
- tf.py_func inside data readers
- Variables and Placeholders dynamic shapes inside graph

