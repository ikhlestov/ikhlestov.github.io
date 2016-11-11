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
and `Coursera ML Courses <https://www.coursera.org/learn/machine-learning>`__. They may seems to be some way unstructured, but work still in progress, so please be patient.

.. contents:: Contents:

Ֆ General Approach
==================

* Define network architecture
* Choose right cost function
* Calculate gradient descent if necessary
* Train, tune hyperparameters.


Ֆ Part I
========

An idea of *stochastic gradient descent* is to estimate the gradient 
:math:`\nabla C` by computing :math:`\nabla Cx` for a small sample of randomly chosen training inputs,
not for all inputs as usual *gradient descent* do.
For this stochastic gradient descent take small number of *m* randomly chosen training inputs.
We'll label those random training inputs :math:`X1,X2,… ,Xm` and refer to them as a *mini-batch*.
So now gradinet can be computed as:  

.. math::
    \nabla C \approx \frac{1}{m}\sum_{j=1}^m \nabla C_{X_j}


Ֆ Part II
=========

.. image:: /images/ML_notes/weights_notation.png

image from `this book <http://neuralnetworksanddeeplearning.com/chap2.html>`__

*Elementwise* product of the two vectors denoted as :math:`s \odot t` and can be called sometimes *Hadamard product* or *Schur product*.  
Her is an example:

.. math::
  \left[\begin{array}{c} 1 \\\ 2 \end{array}\right] 
    \odot \left[\begin{array}{c} 3 \\\ 4\end{array} \right]
  = \left[ \begin{array}{c} 1 * 3 \\\ 2 * 4 \end{array} \right]
  = \left[ \begin{array}{c} 3 \\\ 8 \end{array} \right]

In tensorflow you should distinguish usual matrix multiplication and hadamard product

.. code-block:: python

  # W, Q - some matrices
  
  # matrix multiplication
  res = math_ops.matmul(W, Q)
  
  # hadamard product
  res = W * Q


Ֆ Part III
==========

Regularization
--------------

---------------------------------
Weight decay or L2 regularization
---------------------------------

The idea of L2 regularization is to add an extra term to the cost function, a term called the *regularization term*.

.. math::
  
  C = C_0 + \frac{\lambda}{2n} \sum_w w^2

Where :math:`C_0` is the original cost, second part - regularization term itself
(namely the sum of the squares of all the weights in the network).
This is scaled by a factor :math:`\frac{\lambda}{2n}`, where :math:`\lambda > 0` is
known as *regularization parameter*, and :math:`n` is, as ususal, the size of our
training set.

*Weight decay* factor - :math:`1-\frac{\eta\lambda}{n}`.
So during training on larger dataset we should change :math:`\lambda` with respect
to learning rate and size of training set.

How to choose a neural network's hyper-parameters?
--------------------------------------------------

--------------
Broad strategy
--------------

+ Simplify the model
+ Reduce classification classes
+ Reduce training/validation data
+ Increase frequency of monitoring
+ With such updates you may try to find required hyper-parameters very fast

---------------------
Learning rate (**η**)
---------------------

+ Estimate the threshold value for **η** at which the cost on the training data immediately begins decreasing, instead of oscillating or increasing.

+ After you likely want to use value of **η** that is smaller, say, a factor of two bellow the threshold.

--------------------
Using early stopping
--------------------

A better rule is to terminate if the best classification accuracy doesn't improve for quite some time.
For example we might elect to terminate if the classification accuracy hasn't improved during the last ten epochs.

----------------------
Learning rate schedule
----------------------

We need choose when learning rate should be decreased and by what rule. Some of existing rules are:

+ **Step decay** - reduce learning rate by some factor.
+ **Exponental decay** - :math:`\alpha = \alpha_0 e^{-k t}`, where :math:`\alpha_0, k` are hyperparameters and :math:`t` is the iteration number (but you can also use units of epochs).
+ **1/t decay** - :math:`\alpha = \alpha_0 / (1 + k t )`, where :math:`\alpha_0, k` are hyperparameters and :math:`t` is the iteration number.

Also you may checked `predefined learning schedules at tensorflow <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/training/learning_rate_decay.py>`__.
But prior to use learning rate schedule it's better to get best performed model with fixed learning rate.

---------------
Mini-batch size
---------------

Wights updates for online learning can be declarated as:

.. math::

   w \rightarrow w' = w-\eta \nabla C_x

For case of mini-batch of size 100 we get:

.. math::

  w \rightarrow w' = w-\eta \frac{1}{100} \sum_x \nabla C_x

With this we may increase learning rate by a factor 100 and updated rules become:

.. math::
  
  w \rightarrow w' = w-\eta \sum_x \nabla C_x

With choosing mini-batch size we shouldn't update any others hyper-parameters, only learning rate should be checked. After we may try different mini-batches sizes, scaling learning rate as required and choose what validation accuracy updates faster at real time(not related to epochs) in order to maximize our model overall speed.

--------------------
Automated techniques
--------------------

For automated hyper-parameters choose we can use
`grid search <http://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf>`__
or something like
`Bayesian approach <http://papers.nips.cc/paper/4522-practical-bayesian-optimization-of-machine-learning-algorithms.pdf>`__
(`source code <https://github.com/jaberg/hyperopt>`__)

--------------
Futher reading
--------------

+ `Practical recommendations for gradient-based training of deep architectures <https://arxiv.org/pdf/1206.5533v2.pdf>`__
+ `Efficient BackProp <http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf>`__
+ `Neural Networks: Tricks of the Trade <http://www.springer.com/gp/book/9783642352881>`__ (you may try not to use hwole book, but search for some articles from its authors)

Ֆ Evaluation of algorithm
=========================

What we should do:

1. Split the dataset into three portions: train set, validate set and test set, in a proportion 3:1:1.

2. When the number of examples *m* increase, the cost :math:`{J_{test}}` increases, while :math:`{J_{val}}` decrease. When *m* is very large, if :math:`{J_{test}}` is about equal to :math:`{J_{val}}` the algorithm may suffer from large bias(underfiting), while if there is a gap between :math:`{J_{test}}` and :math:`{J_{val}}` the algorithm may suffer from large variance(overfitting).

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

Ֆ Overfiting and underfitting
=============================

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
