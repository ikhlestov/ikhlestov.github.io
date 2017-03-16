.. title: Linear classification
.. slug: 2_linear_classification
.. date: 2016-12-15 21:55:43 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents:

The approach will have two major components:
a **score function** that maps the raw data to class scores,
and a **loss function** that quantifies the agreement between the predicted scores and the ground truth labels.
We will then cast this as an optimization problem in which we will minimize the loss function with respect to the parameters of the score function.

Parameterized mapping from images to label scores
=================================================

We have training dataset of images :math:`x_i \in R^D`, each associated with label :math:`y_i`.
Here :math:`i = 1 \dots N`, where :math:`N` - num examples, and
:math:`y_i \in { 1 \dots K }`, where :math:`K` - num classes.
We will now define the score function :math:`f: R^D \mapsto R^K` that maps the raw image pixels to class scores.

Linear classifier
-----------------

Can be defined as:

.. math::

    f(x_i, W, b) =  W x_i + b

Every row of :math:`W` became a classifier for one of the classes.

**Interpretation of linear classifiers as template matching**. Another interpretation for the weights :math:`W` is that each row of :math:`W` corresponds to a template (or sometimes also called a prototype) for one of the classes.
Another way to think of it is that we are still effectively doing Nearest Neighbor, but instead of having thousands of training images we are only using a single image per class (although we will learn it, and it does not necessarily have to be one of the images in the training set).

Bias trick
----------

A commonly used trick is to combine the two sets of parameters into a single matrix that holds both of them by extending the vector :math:`x_i` with one additional dimension that always holds the constant :math:`1` - a *default bias dimension*. With the extra dimension, the new score function will simplify to a single matrix multiply:

.. math::

    f(x_i, W) =  W x_i

Image data processing
---------------------

It is important to **center your data** by subtracting the mean from every feature.
In the case of images, this corresponds to computing a mean image across the training images and subtracting it from every image to get images where the pixels range from approximately [-127 … 127]. 
Further common preprocessing is to scale each input feature so that its values range from [-1, 1] (divide by standard deviation).

Loss function
=============

We are going to measure correctness of outcomes classes with a **loss function** (or sometimes also referred to as the **cost function** or the **objective**).

Multiclass Support Vector Machine loss
--------------------------------------

As a first example we will first develop a commonly used loss called the **Multiclass Support Vector Machine** (SVM) loss.
The SVM loss is set up so that the SVM “wants” the correct class for each image to a have a score higher than the incorrect classes by some fixed margin :math:`\Delta` .


The score function takes the pixels and computes the vector :math:`f(x_i,W)` of class scores, which we will abbreviate to :math:`s` (short for scores).
For example, the score for the j-th class is the j-th element: :math:`s_j = f(x_i, W)_j` .
The Multiclass SVM loss for the i-th example is then formalized as follows:

.. math::

    L_i = \sum_{j\neq y_i} \max(0, s_j - s_{y_i} + \Delta)

**Example.**
Suppose that we have three classes that receive the scores :math:`s=[13,−7,11]` , and that the first class is the true class (i.e. :math:`y_i=0` ).
Also assume that :math:`\Delta = 10` .
The expression above sums over all incorrect classes :math:`j \neq y_i` , so we get two terms:

.. math::

    L_i = \max(0, -7 - 13 + 10) + \max(0, 11 - 13 + 10) = 8

In summary, the SVM loss function wants the score of the correct class :math:`y_i` to be larger than the incorrect class scores by at least by :math:`\Delta` (delta).

We can also rewrite the loss function in this equivalent form:

.. math::

    L_i = \sum_{j\neq y_i} \max(0, w_j^T x_i - w_{y_i}^T x_i + \Delta)

where :math:`w_j` is the j-th row of the :math:`W` reshaped as a column.

A last piece of terminology we’ll mention before we finish with this section is that the threshold at zero :math:`max(0, -)` function is often called **hinge loss**.
You’ll sometimes hear about people instead using the squared hinge loss SVM (or L2-SVM), which uses the form :math:`max(0,−)^2` that penalizes violated margins more strongly (quadratically instead of linearly)

Regularization
--------------

There might be many similar :math:`W` that correctly classify the examples. To get such weights we may just multiply existing weights by some scalar :math:`\lambda > 1`, such as :math:`\lambda W`.

We wish to encode some preference for a certain set of weights :math:`W` over others to remove this ambiguity.
We can do so by extending the loss function with a **regularization penalty** :math:`R(W)`.
The most common regularization penalty is the **L2** norm that discourages large weights through an elementwise quadratic penalty over all parameters:

.. math::

    R(W) = \sum_k\sum_l W_{k,l}^2

Including the regularization penalty completes the full Multiclass Support Vector Machine loss, which is made up of two components: the **data loss** and the **regularization loss**.

.. math::

    L =  \underbrace{ \frac{1}{N} \sum_i L_i }_\text{data loss} + \underbrace{ \lambda R(W) }_\text{regularization loss} \\\\

Or expanding this out in its full form:

.. math::

    L = \frac{1}{N} \sum_i \sum_{j\neq y_i} \left[ \max(0, f(x_i; W)_j - f(x_i; W)_{y_i} + \Delta) \right] + \lambda \sum_k\sum_l W_{k,l}^2

Where :math:`N` is the number of training examples. As you can see, we append the regularization penalty to the loss objective, weighted by a hyperparameter :math:`\alpha`.
There is no simple way of setting this hyperparameter and it is usually determined by cross-validation.

The most appealing property is that penalizing large weights tends to improve generalization, because it means that no input dimension can have a very large influence on the scores all by itself.
(Also check `full lecture notes <http://cs231n.github.io/linear-classify/>`__ explanation why mentioned behavior exits.)

Softmax classifier
==================

The other popular choice is the **Softmax classifier**, which has a different loss function.
Unlike the SVM which treats the outputs :math:`f(x_i,W)` as (uncalibrated and possibly difficult to interpret) scores for each class, the Softmax classifier gives a slightly more intuitive output (normalized class probabilities) and also has a probabilistic interpretation that we will describe shortly.
We will replace the *hinge loss* with a **cross-entropy loss** that has the form:

.. math::

    L_i = -\log\left(\frac{e^{f_{y_i}}}{ \sum_j e^{f_j} }\right) \hspace{0.5in} \text{or equivalently} \hspace{0.5in} L_i = -f_{y_i} + \log\sum_j e^{f_j}

where we are using the notation :math:`f_j` to mean the j-th element of the vector of class scores :math:`f`.
The function :math:`f_j(z) = \frac{e^{z_j}}{\sum_k e^{z_k}}` is called the **softmax function**: It takes a vector of arbitrary real-valued scores (in :math:`z` ) and squashes it to a vector of values between zero and one that sum to one.

**Information theory view.**
The *cross-entropy* between a "true" distribution :math:`p` and an estimated distribution :math:`q` is defined as:

.. math::

    H(p,q) = - \sum_x p(x) \log q(x)

The Softmax classifier is hence minimizing the cross-entropy between the estimated class probabilities ( :math:`q = e^{f_{y_i}}  / \sum_j e^{f_j}` as seen above)
and the "true" distribution, which in this interpretation is the distribution where all probability mass is on the correct class (i.e. :math:`p=[0,…1,…,0]` contains a single 1 at the :math:`y_i` -th position.).
Moreover, since the cross-entropy can be written in terms of entropy and the Kullback-Leibler divergence as :math:`H(p,q) = H(p) + D_{KL}(p||q)` ,
and the entropy of the delta function :math:`p` is zero, this is also equivalent to minimizing the KL divergence between the two distributions (a measure of distance).
In other words, the cross-entropy objective *wants* the predicted distribution to have all of its mass on the correct answer.

**Probabilistic interpretation.** Looking at the expression, we see that

.. math::

    P(y_i \mid x_i; W) = \frac{e^{f_{y_i}}}{\sum_j e^{f_j} }

can be interpreted as the (normalized) probability assigned to the correct label :math:`y_i` given the image :math:`x_i` and parameterized by :math:`W`.
To see this, remember that the Softmax classifier interprets the scores inside the output vector :math:`f` as the unnormalized log probabilities.
Exponentiating these quantities therefore gives the (unnormalized) probabilities, and the division performs the normalization so that the probabilities sum to one.
In the probabilistic interpretation, we are therefore minimizing the negative log likelihood of the correct class, which can be interpreted as performing *Maximum Likelihood Estimation* (MLE).
A nice feature of this view is that we can now also interpret the regularization term :math:`R(W)` in the full loss function as coming from a Gaussian prior over the weight matrix :math:`W`,
where instead of MLE we are performing the *Maximum a posteriori* (MAP) estimation.

**Practical issues: Numeric stability.**
When you’re writing code for computing the Softmax function in practice, the intermediate terms :math:`e^{f_{y_i}}` and :math:`\sum_j e^{f_j}` may be very large due to the exponentials.
But if we multiply the top and bottom of the fraction by a constant :math:`C` and push it into the sum, we get the following (mathematically equivalent) expression:

.. math::

    \frac{e^{f_{y_i}}}{\sum_j e^{f_j}}
    = \frac{Ce^{f_{y_i}}}{C\sum_j e^{f_j}}
    = \frac{e^{f_{y_i} + \log C}}{\sum_j e^{f_j + \log C}}

We are free to choose the value of :math:`C`.
This will not change any of the results, but we can use this value to improve the numerical stability of the computation.
A common choice for :math:`C` is to set :math:`\log C = -\max_j f_j`.
This simply states that we should shift the values inside the vector :math:`f` so that the highest value is zero.

.. code-block:: python

    f = np.array([123, 456, 789]) # example with 3 classes and each having large scores
    p = np.exp(f) / np.sum(np.exp(f)) # Bad: Numeric problem, potential blowup

    # instead: first shift the values of f so that the highest number is 0:
    f -= np.max(f) # f becomes [-666, -333, 0]
    p = np.exp(f) / np.sum(np.exp(f)) # safe to do, gives the correct answer


**Possibly confusing naming conventions.**
To be precise, the *SVM classifier* uses the *hinge loss*, or also sometimes called the *max-margin loss*.
The *Softmax classifier* uses the *cross-entropy loss*.

Softmax classifier provides “probabilities” for each class
==========================================================

We put the word “probabilities” in quotes, however, is that how peaky or diffuse these probabilities are depends directly on the regularization strength :math:`\lambda` - which you are in charge of as input to the system.
For example, suppose that the unnormalized log-probabilities for some three classes come out to be [1, -2, 0]. The softmax function would then compute:

.. math::

    [1, -2, 0] \rightarrow [e^1, e^{-2}, e^0] = [2.71, 0.14, 1] \rightarrow [0.7, 0.04, 0.26]

Where the steps taken are to exponentiate and normalize to sum to one.
Now, if the regularization strength :math:`\alpha` was higher, the weights :math:`W` would be penalized more and this would lead to smaller weights.
For example, suppose that the weights became one half smaller ([0.5, -1, 0]). The softmax would now compute:

.. math::

    [0.5, -1, 0] \rightarrow [e^{0.5}, e^{-1}, e^0] = [1.65, 0.37, 1] \rightarrow [0.55, 0.12, 0.33]

where the probabilites are now more diffuse.
Moreover, in the limit where the weights go towards tiny numbers due to very strong regularization strength :math:`\alpha`, the output probabilities would be near uniform.


