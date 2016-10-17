.. title: Models Architectures
.. slug: models-architectures
.. date: 2016-10-17 13:13:34 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents:

RNN \+ HighWay \+ CNN
=====================

This models was proposed for text representation: `paper <https://arxiv.org/pdf/1606.06905.pdf>`__.

.. figure:: /images/models_architectures/rnn_highway_cnn.png

    `image source <https://arxiv.org/pdf/1606.06905.pdf>`__

RNN \+ Attention(Google Translate)
==================================

Google's Neural Machine Translation System:
`paper <https://arxiv.org/pdf/1609.08144v2.pdf>`__, 
`blog <https://research.googleblog.com/2016/09/a-neural-network-for-machine.html>`__.
Interesting approaches were used:

+ They provide stacked LSTM with residual connections: input to the next layer is output from previous one element wise summed with initial input.
+ Train model first with Adam optimizer, and after with simple SGD.

.. figure:: /images/models_architectures/rnn_attention.png

    `image source <https://arxiv.org/pdf/1609.08144v2.pdf>`__
