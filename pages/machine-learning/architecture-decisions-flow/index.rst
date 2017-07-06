.. title: Architecture Decisions Flow
.. slug: architecture-decisions-flow
.. date: 2017-07-06 17:13:58 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents::

Data Augmentation
=================

- Train network to one image size(224x224) and fine tune after for less epochs to larger size(448x448 for example)
- Train image detection network with image classification dataset

Initialization
==============

- Random
- Xavier

`Activation functions <https://en.wikipedia.org/wiki/Activation_function>`__
=============================================================================

- Sigmoid
- ReLU
- Leaky ReLU
- ELU
- `SELU <https://arxiv.org/pdf/1706.02515.pdf>`__

Loss functions
==============

- hinge loss :math:`L_i = \sum_{j\neq y_i} \max(0, s_j - s_{y_i} + \Delta)`
- cross-entropy loss
- Triplet-loss - multi class loss from `FaceNet <https://arxiv.org/abs/1503.03832>`__
- Center-loss - from `this paper <http://ydwen.github.io/papers/WenECCV16.pdf>`__
- Angular Softmax - from `Sphere Face <https://arxiv.org/abs/1704.08063>`__

Regularization
=======================

- Dropout
- GaussianDropout
- L1, L2, Lp
- Label smoothing

Normalization
===================

- Batch Norm
- Layer Norm
- Weight Norm
- Fusing parameters(???)

Optimizers
==========

- First order

  - Gradient Descent
  - Momentum
  - Adam

- Second order

Convolutions
============

- Usual convolutions
- 3x3 is better
- 1x1 convolutions from `Network-in-network(NiN) <https://arxiv.org/abs/1312.4400>`__
- Flattened convolutions(Cx1, 1xC kernels)(`Paper <https://arxiv.org/abs/1412.5474>`__)
- depthwise separable convolutions(`Xception <https://arxiv.org/abs/1610.02357>`__)

  - 1x1 convs and then separable by channels 3x3 convs
  - Separable by channels 3x3 convs and after 1x1 convs for all features

- Grouped convolutions (initially in AlexNet, updated in `ResNeXt <https://arxiv.org/abs/1611.05431>`__)
- Shuffled Grouped Convolutions(`Shuffle Net <https://arxiv.org/abs/1707.01083v1>`__)

Another architectures decisions
===============================

- Average pooling as part of the last classifier
- Use conv with stride without overlapping, not average/max pooling
- Inception module(parallel computation of various filters with 1x1 convs and after concatenating them)
- Bypassing features over two layers(as in ResNet or HighwayNets)
- Concatenating features from current layer with features from previous ones(as in DenseNet)
- Combine Inception Block with DenseNet approach

.. Selection of hyperparameters
.. ============================


A systematic evaluation of CNN modules
=======================================

- `Link to initial paper <https://arxiv.org/pdf/1606.02228.pdf>`__
- use ELU non-linearity without batchnorm or ReLU with it.
- apply a learned color space transformation of RGB.
- use the linear learning rate decay policy.
- use a sum of the average and max pooling layers.
- use mini-batch size around 128 or 256. If this is too big for your GPU, decrease the learning rate proportionally to the batch size.
- use fully-connected layers as convolutional and average the predictions for the final decision.
- when investing in increasing training set size, check if a plateau has not been reach.
- cleanliness of the data is more important then the size.
- if you cannot increase the input image size, reduce the stride in the consequent layers, it has roughly the same effect.
- if your network has a complex and highly optimized architecture, like e.g. GoogLeNet, be careful with modifications.
