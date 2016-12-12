.. title: ML Knowledge Base
.. slug: ml-knowledge-base
.. date: 2016-11-11 16:14:43 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents:

Definitions
=============

One-shot learning
    aim to lean not from thousands of examples but from one or only a few.

Transfer learning
    apply already trained model with previous knowledge to the new domain.

MLP
    is an abbreviation for *multilayer perceptrons*  

Computational neuroscience
    is primarily concerned with building more accurate models of how the brain actually works.


Activation Functions
====================

# TODO: add why they different and what types better for what tasks

Allow us add some nonlinearity to the model and to produce a non-linear decision boundary.
So the combination of weights coefficients will not "generalized" to linear model.
More about another types of activations you may read `here <https://en.wikipedia.org/wiki/Activation_function>`__.

Sigmoid function (or *logistic function*) 
    .. math::

        \sigma(z) = \frac{1}{1 + e^{-z}}
    
    Properties: :math:`\sigma(\infty)\approx 1`, :math:`\sigma(-\infty)\approx 0`,
    but note, that :math:`\sigma(0)=1`.  

    Note: *sigmoid function* (:math:`\sigma`) == *logistic function*
    so *sigmoid neurons* can be called as *logistic neurons*.
    
    Generate probability for discrete classification tasks in which each class is
    independent and not mutually exclusive.
    For instance a picture can contain both an elephant and a dog at the same time.


Softmax function
    .. math::

      a^L_j = \frac{e^{z^L_j}}{\sum_k e^{z^L_k}}

    The output activations from softmax are guaranteed to always sum up to 1.
    
    Generate probability for discrete classification tasks in which the classes 
    are mutually exclusive (each entry is in exactly one class).
    For instance a picture can contain elephant or dog, not both.



Cost Functions
==============

Note that cost function should be non negative!  

Cost function also can be called as *loss function* or *objective function*.

Quadratic cost function
    :math:`C = \frac{1}{2n}\sum_{n}(y - a)^2`

    + :math:`y` - the target output
    + :math:`a` - the network output
    + :math:`n` - the total number of training inputs

    Can be called as *mean squared error*, or just *MSE*.

Cross-entropy cost function
    :math:`C = -\frac{1}{n} \sum_x \left[y_t \ln y_o + (1-y_t ) \ln (1-y_o) \right]`  

    + :math:`n` - the total number of items of training data
    + :math:`x` - the sum is over all training inputs
    + :math:`y_t` - corresponding target output
    + :math:`y_o` - the network output(predicted values). Can be replaced with :math:`a`.

Regularization approaches
=========================

L1 regularization
    to be filled

L2 regularization
    to be filled

Dropout
    to be filled


Evaluation metrics
==================

to be filled
