.. title: Quick Reference
.. slug: quck_ref
.. date: 2017-03-13 17:08:21 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents:

Math
====

Matrix multiplication
---------------------
.. image:: https://wikimedia.org/api/rest_v1/media/math/render/svg/780671bdfb3fab93187156d2c226df6fe36746fe

.. figure:: https://wikimedia.org/api/rest_v1/media/math/render/svg/24e439c972de89fb94297419cab45c58f1a32c43


.. code-block:: python

    # shape (2, 3)
    A = [[1, 2, 3],
         [4, 5, 6]]
    # shape (3, 2)
    B = [[7, 8],
         [9, 10],
         [11, 12]]

    # shape (2, 2)
    Z = [[1 * 7 + 2 * 9 + 3 * 11, 1 * 8 + 2 * 10 + 3 * 12],
         [4 * 7 + 5 * 9 + 6 * 11, 4 * 8 + 5 * 10 + 6 * 12]]
    # multiply row of A by the column of B and sum the result
    Z[i, j] = sum(A[i] * B[:, j])

.. figure:: https://wikimedia.org/api/rest_v1/media/math/render/svg/c6f7cdbe9cd36a436b0e5304ea2b42d640203777

.. figure:: https://wikimedia.org/api/rest_v1/media/math/render/svg/5f877a81f2a22a2109790c35f6c11bf85af22b82

Logarithms / Exponents
----------------------

.. math::

    \ln (e ^ x) = x

    \log_{a} (a ^ x) = x

.. image:: https://s-media-cache-ak0.pinimg.com/originals/bd/b0/ce/bdb0ce6d9c5a6e2a8006e639ee01202b.jpg

Derivatives
-----------

.. image:: http://www.mathspadilla.com/matII/Unit3-Derivatives/deriv11.png


.. image:: https://www.eeweb.com/tools/math-sheets/images/calculus-derivatives-limits.png

Statistics
==========

standard deviation - square root of variance. :math:`std = \sqrt{variance}`. :math:`\sigma = \sqrt{ \frac{1}{n} \sum_{i=1}^{n}(x_i - x_{mean})^2}`


Activation functions
====================

.. math::

    \textsf{Sigmoid}

    f(x) = \frac{1}{1 + e^{-x}}

    \textsf{Tanh}

    f(x) = \tanh(x) = \frac{2}{1 + e^{-2x}} - 1

    \textsf{Softmax}

    f(x)_i = \frac{e^{x_i}}{\sum_{k=1}^{K} e^{x_k}}


Back propagation / Gradient descent
===================================

Back propagation
----------------

Starting with the final output recursively applies the chain rule to compute the gradients of every layer.
For :math:`L_{i}` layer backprop can be computed as derivative for every element based on :math:`L_{i + 1}` layer backprop output.

Gradient descent
----------------

To find a local minimum of a function using gradient descent, one takes steps proportional to the negative of the gradient (or of the approximate gradient) of the function at the current point.
Gradient - vector containing all of the partial derivatives. This mean in case while computed derivative for one function input, all other stay the same.

Stochastic gradient descent
---------------------------

Perform Gradient Descent only with some part of examples


Validation metrics
==================

Confusion Matrix - matrix contains True/False positives/negatives.

Precision: :math:`\frac{{TruePositive}}{{TruePositive + FalsePositive}}`.
Put another way, it is the number of positive predictions divided by the total number of positive class values predicted.
A low precision can also indicate a large number of False Positives.
*How many selected items are relevant*

Recall: :math:`\frac{{TruePositive}}{{TruePositive + FalseNegtive}}`.
Put another way it is the number of positive predictions divided by the number of positive class values in the test data.
Recall can be thought of as a measure of a classifiers completeness. A low recall indicates many False Negatives.
*How many relevant items are selected*

F1 score: :math:`\frac{{2*Recall*Precision}}{{Recall + Precision}}` balanced precision and recall.

kNN and k-means
===============

**kNN(k-nearest neighbors algorithm)** - classification algorithm when class of undefined element will be issued based on classes of K nearest neighbors.

**k-means** - clusterization algorithm. Aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster:

- Define k clusters

- Calculate distance to every point

- Assign each pending point to the nearest cluster

- Recalculate new clusters centers

- Recalculate new distances: :math:`v_i = (1/c_i) \sum_{j=1}^{c_i} x_i`, where :math:`c_i` represents number of data points in :math:`i^{th}` cluster.

- If no any points were reassigned - stop iterations

Covariance and correlation
==========================

Both describe the degree to which two random variables or sets of random variables tend to deviate from their expected values in similar ways.

If :math:`X` and :math:`Y` are two random variables, with means (expected values) :math:`\mu_X` and :math:`\mu_Y` and standard deviations :math:`\sigma_X` and :math:`\sigma_Y`, respectively, then their covariance and correlation are as follows:

.. figure:: https://wikimedia.org/api/rest_v1/media/math/render/svg/5f6328c2a98e12b74140dfc6fb614f7939e12a1c

    Covariance

.. figure:: https://wikimedia.org/api/rest_v1/media/math/render/svg/c8ad7d4bca4314703d33deb0245732bcc249dfa4

    Correlation

where :math:`E[ ]` is the expected value, also known as the mean.

PCA
===

Principal components - components with most variation, directions where the data is most spread out.

Eigenvectors and values exist in pairs: every eigenvector has a corresponding eigenvalue. An eigenvector is a direction.
An eigenvalue is a number, telling you how much variance there is in the data in that direction, in the example above the eigenvalue is a number telling us how spread out the data is on the line.
The eigenvector with the highest eigenvalue is therefore the principal component.

In fact the amount of eigenvectors/values that exist equals the number of dimensions the data set has.

Reducing dimension performed by stripping some eigenvectors with small eigenvalues. Only eigenvectors with large eigenvalues remains.

Also Multiple Discriminant Analysis(MDA) approach exist. In MDA we are additionally interested to find the directions that maximize the separation (or discrimination) between different classes (for example, in pattern classification problems where our dataset consists of multiple classes. In contrast two PCA, which ignores the class labels).

PCA step by step:

- Compute means of every dimension.

- Compute the scatter matrix :math:`S = \sum\limits_{k=1}^n (\pmb x_k - \pmb m)\;(\pmb x_k - \pmb m)^T`, where :math:`\pmb m` is the mean vector.

- Or alternatively compute covariance matrix (numpy.cov function) (a matrix whose element in the i, j position is the covariance between the :math:`i^{th}` and :math:`j^{th}` elements of a random vector).

- Compute eigenvectors/ eigenvalues: ``eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)``

  + Eigenvalues :math:`\alpha` can be obtained by solving an equation :math:`|\textbf{A} - \alpha \textbf{I}| = 0`, where :math:`\textbf{A}` is a matrix and :math:`| |` means determinant.

  + Eigenvectors :math:`\pmb v` than can be obtained by :math:`(\textbf{A} - \alpha_j \textbf{I})\pmb v_j = 0`.

- We can check correctness of eigenvectors/eigenvalues as :math:`\pmb\Sigma\pmb{v} = \lambda\pmb{v}`, where :math:`\pmb\Sigma` - covariance matrix, :math:`\pmb{v}` - eigenvector, :math:`\lambda` - eigenvalue.

- Sorting the eigenvectors by decreasing eigenvalues

- Choosing k eigenvectors with the largest eigenvalues and receive :math:`\pmb W` matrix.

- To receive dimension reduction we should only compute :math:`\pmb y = \pmb W^T \times \pmb x`

L1/ L2 normalization
====================

The idea of regularization is to add an extra term to the cost function, a term called the regularization term.

Regularization term for :math:`L_p` norm can be computed as :math:`||x||_{p}=(\sum_{i}|x_{i}|^{p})^{1/p}`.

Great explanation can be found `on stackoverflow <http://stackoverflow.com/questions/32276391/feature-normalization-advantage-of-l2-normalization>`__ 
or `here <http://stats.stackexchange.com/questions/163388/l2-regularization-is-equivalent-to-gaussian-prior>`__

Subgradient
===========

Something used for not differentiable functions. SHould be filled.
