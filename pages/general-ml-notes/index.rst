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

High **bias** is **underfitting** and high **variance** is **overfitting**.  

For understanding what exactly mean *Bias* and *Variance* you may check `this <http://scott.fortmann-roe.com/docs/BiasVariance.html>`__
or `this <http://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/>`__
cool articles.  

Next notes based on awesome Andre Ng `lecture <https://www.youtube.com/watch?v=F1ka6a13S9I>`__  

During training as usual you split your data on train, validation and test sets.
*Note:* You should keep your validation/test data the same for model you want to compare.
After measuring errors you can get some results.
In this case difference between *human error* (how human perform such task) and *train error* will be **bias**.
On the other hand, difference between *train error* and *validation error* will be **variance**.

.. image:: /images/ML_notes/bias_variance_explanation_1.svg 
   :width: 320 px
   :height: 120 px
   :alt: bias_variance_explanation_1

In such case you should consider this methods

.. image:: /images/ML_notes/bias_variance_workflow_1.svg 
   :width: 443 px
   :height: 402 px
   :alt: bias_variance_workflow_1

Solutions inside blue boxes should be applied as first approach.  

But sometimes you may have a lot of data from one domain, but test data comes from another.
In this case validation and test data should be from the same domain.
Also you may consider get validation data also from large domain.
But it should be additional validation(say *train-valid*).
Let's see an example.

.. image:: /images/ML_notes/data_spliting_in_domains.svg 
   :width: 473 px
   :height: 93 px
   :alt: data_spliting_in_domains

In this case we receive another correlation between errors: 

.. image:: /images/ML_notes/bias_variance_explanation_2.svg 
   :width: 453 px
   :height: 166 px
   :alt: bias_variance_explanation_2

And solution algorithm will be a little bit more longer:

.. image:: /images/ML_notes/bias_variance_workflow_2.svg 
   :width: 443 px
   :height: 675 px
   :alt: bias_variance_workflow_2

