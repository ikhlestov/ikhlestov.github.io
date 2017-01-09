.. title: Batch Normalization
.. slug: batch-normalization
.. date: 2016-12-23 15:24:34 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

Notes based on `this paper <https://arxiv.org/pdf/1502.03167v3.pdf>`__. I think to understood BN enough just quickly pass through 3rd paragraph.

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

    inputs = tf.sigmoid(tf.contrib.layers.batch_norm(inputs, scale=True))

    # next lines should be added so Optimizer can find variables to optimize
    update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
    if update_ops:
        updates = tf.group(*update_ops)
        total_loss = control_flow_ops.with_dependencies([updates], total_loss)
