.. title: Different types of the convolution layers
.. slug: convolutions-types
.. date: 2017-07-07 14:17:58 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov


If you are looking for explanation what convolution layers are, it better to check :doc:`convolutional-layers` page

.. contents::

Simple Convolution
==================

Take multiply dot products with same filter with some width/height shift. Interesting because:

- Weights sharing
- Translation invariant

.. figure:: /images/ML_notes/convolutions/01_simple_convolution.jpg
    

1x1 Convolutions
================

Initially 1x1 convolutions were proposed at `Network-in-network(NiN) <https://arxiv.org/abs/1312.4400>`__.
After they were highly used in `GoogleNet architecture <https://arxiv.org/abs/1409.4842>`__.
Main features of such layers:

- Reduce or increase dimensionality
- Apply nonlinearity again after convolution
- Can be considered as "feature pooling"

They are used in such way: we have image with size 32x32x100, where 100 means features, and after applying 20 1x1 convolutions filters we will get images with 32x32x20 dimensions.

.. figure:: /images/ML_notes/convolutions/02_1x1_convs.png

Flattened Convolutions
======================

Were published in `Flattened Convolutional Neural Networks for Feedforward Acceleration <https://arxiv.org/abs/1412.5474>`__.
Reason of usage same as 1x1 convs from NiN networks, but now not only features dimension set to 1, but also one of another dimensions: width or height.

.. figure:: /images/ML_notes/convolutions/03_flattened_convs.png


Spatial and Cross-Channel convolutions
======================================

First this approach was widely used in Inception network.
Main reason is to split operations for cross-channel correlations and at spatial correlations into a series of independently operations.
Spatial convolutions means convolutions performed in **spatial dimensions** - **width** and **height**.

.. image:: /images/ML_notes/convolutions/04_simple_inception.png

Depthwise Separable Convolutions
=========================================================

A lot about such convolutions published in the (`Xception paper <https://arxiv.org/abs/1610.02357>`__) or
(`MobileNet paper <https://arxiv.org/abs/1704.04861>`__).
Consist of:

- **Depthwise convolution**, i.e. a spatial convolution performed independently over each channel of an input.
- **Pointwise convolution**, i.e. a 1x1 convolution, projecting the channels output by the depthwise convolution onto a new channel space.

Difference between Inception module and separable convolutions:

- Separable convolutions perform first channel-wise spatial convolution and then perform 1x1 convolution, whereas Inception performs the 1x1 convolution first.
- depthwise separable convolutions are usually implemented without non-linearities.

.. image:: /images/ML_notes/convolutions/05_1_deepwise_convolutions.png


Grouped Convolutions
====================

Grouped convolutions were initial mentioned in AlexNet, and later reused in `ResNeXt <https://arxiv.org/abs/1611.05431>`__.
Main motivation of such convolutions is to reduce computational complexity while dividing features on groups.

.. image:: /images/ML_notes/convolutions/05_2_group_convolutions.png

Shuffled Grouped Convolutions
==============================

`Shuffle Net <https://arxiv.org/abs/1707.01083>`__ proposed how to eliminate main side effect of the grouped convolutions that "outputs from a certain channel are only derived from a small fraction of input channels".

They proposed shuffle channels in such way(layer with :math:`g` groups whose output has :math:`g × n` channels):

- reshape the output channel dimension into :math:`(g, n)`
- transpose output
- flatten output back

.. image:: /images/ML_notes/convolutions/06_shuffled_grouped_convolutions.png

So at the end in paper was proposed to use such convolutions for 1x1 convolutions to reduce computation costs. Notice, that 3x3 convolutions still usual depthwise approach and last operation was changed from *Add* to *Concat*.

.. image:: /images/ML_notes/convolutions/07_shuffled_grouped_convolutions_usage.png
