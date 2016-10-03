.. title: General ML Notes
.. slug: general-ml-notes
.. date: 2016-10-02 23:00:05 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

This notes based on `Neural Networks and Deep Learning <http://neuralnetworksanddeeplearning.com/index.html>`__
and `Coursera ML Courses <https://www.coursera.org/learn/machine-learning>`__. They may seems to be some way unstructured, but such structure is useful for me.

.. contents:: Contents:

General Approach
================

* Define network architecture
* Choose right cost function
* Calculate gradient descent if necessary
* Train, tune hyperparameters.

Part I
======

Sigmoid function: 

.. math::
    
    \sigma(z) = \frac{1}{1 + e^{-z}}
    
:math:`\sigma(\infty)\approx 1`, :math:`\sigma(-\infty)\approx 0`, 
but note, that :math:`\sigma(0)=1`  

Note: *sigmoid function* (:math:`\sigma`) == *logistic function*
so *sigmoid neurons* can be called as *logistic neurons*.  

**MLP** is an abbreviation for *multilayer perceptrons*  

*cost* fucntion == *loss* function == *objective* function.  

*Quadratic cost function* (or *mean squared error*, or just *MSE*):  

.. math::

    C(w,b)  = \frac{1}{2n}\sum_{n}||y(x) - a||^2

Here,
*w* denotes the collection of all weights in the network,
*b* all the biases,
*n* is the total number of training inputs,
*a* is the vector of outputs from the network when *x* is input,
and the sum is over all training inputs, *x*.  

An idea of *stochastic gradient descent* is to estimate the gradient 
:math:`\nabla C` by computing :math:`\nabla Cx` for a small sample of randomly chosen training inputs,
not for all inputs as usual *gradient descent* do.
For this stochastic gradient descent take small number of *m* randomly chosen training inputs.
We'll label those random training inputs :math:`X1,X2,… ,Xm` and refer to them as a *mini-batch*.
So now gradinet can be computed as:  

.. math::
    \nabla C \approx \frac{1}{m}\sum_{j=1}^m \nabla C_{X_j}


Evaluation of algorithm
=======================

What we should do:

1. Split the dataset into three portions: train set, validate set and test set, in a proportion 3:1:1.

2. When the number of examples *m* increase, the cost :math:`{J_{test}}` increases, while :math:`{J_{val}}` decrease. When *m* is very large, if :math:`{J_{test}}` is about equal to :math:`{J_{val}}` the algorithm may suffer from large bias(underfiting), while if there is a gap between :math:`{J_{test}}` and :math:`{J_{val}}` the algorithm may suffer from large variance(overfiting).

3. To solve the problem of large bias, you may decrease :math:`{\rm{\lambda }}` in regularization, while increase it for the problem of large variance.

4. To evaluate the performance of a classification algorithm, we can use the value: precision, recall and F1.

Precision:

.. math::
    \frac{{TruePositive}}{{TruePositive + FalsePositive}}

Recall:

.. math::
    \frac{{TruePositive}}{{TruePositive + FalseNegtive}}

F1:

.. math::
    \frac{{2*Recall*Precision}}{{Recall + Precision}}

Overfiting and underfiting
==========================

.. thumbnail:: /images/ML_notes/bias_and_variance.jpg  

For understanding what exactly mean *Bias* and *Variance* you may check `this <http://scott.fortmann-roe.com/docs/BiasVariance.html>`__
or `this <http://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/>`__
cool articles.  

To deal with them check this articles:
`Advice for Applying Machine Learning <https://share.coursera.org/wiki/index.php/ML:Advice_for_Applying_Machine_Learning>`__, 
`Machine Learning System Design <https://share.coursera.org/wiki/index.php/ML:Machine_Learning_System_Design>`__,
`Large Scale Machine Learning <https://share.coursera.org/wiki/index.php/ML:Large_Scale_Machine_Learning>`__. 

High **bias** is **underfitting** and high **variance** is **overfitting**.  

Our decision process can be broken down as follows:

* Fixes high variance(overfiting):
    
  * Getting more training examples
  
  * Trying smaller sets of features

* Fixes high bias(underfiting):
    
  * Adding features
    
  * Adding polynomial features

.. thumbnail:: /images/ML_notes/high_variance.png

.. thumbnail:: /images/ML_notes/high_bias.png

When the hypothesis function is too complex 
or there are too many features while the number of training examples is not large enough, 
you may get an overfitting problem. 
In that case, :math:`J\left( \theta \right)` of the training set may be very low, 
while that of the validate set and test set can be high. 
A good method to solve the problem is regularization which adds the squared 
term of parameters to the cost function.
