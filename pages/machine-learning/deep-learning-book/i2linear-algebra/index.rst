.. title: I.2.Linear Algebra
.. slug: i2linear-algebra
.. date: 2016-12-15 21:55:43 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

If you need just quick ref - see `The Matrix CookBook <http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/3274/pdf/imm3274.pdf>`__.
For full book about linear algebra - `Shilov 1977 linear algebra <https://cosmathclub.files.wordpress.com/2014/10/georgi-shilov-linear-algebra4.pdf>`__

Scalars
    is just a single number.

Vectors
    is an array of numbers.

Matrices
    is a 2-D array of numbers, so each element is identified by two indices instead of just one.

Tensors
    an array with more than two axes.

The product operation of matrices(**matrix product**) :math:`C = AB` is defined as :math:`C_{i,j} = \sum_{k} A_{i,k} B_{j,k}`.

Matrix containing the product of the individual elements called the **element-wise product** or **Hadamard product**, and is denoted as :math:`A \odot B`.  

Matrix multiplication is distributive :math:`A(B + C) = AB + AC`. 

Matrix multiplication is associative also :math:`A(BC) = (AB)C`.

Transpose matrix product :math:`(AB)^{T} = B^{T} A^{T}`.

An **identity matrix** is a matrix that does not change any vector when we multiply that vector by that matrix. We denote the identity matrix that preserves
*n*-dimensional vectors as :math:`I_{n}`.

.. math::

    \forall x \in \mathbb{R}, I_{n}x = x

All the entries along the main diagonal in identity matrix is 1, while all other entries are zero.

The **matrix inverse** of :math:`A` is denoted as :math:`A^{−1}` , and it is defined as the matrix such that :math:`A A^{-1} = I_{n}`.

Origin
    the point specified by the vector of all zeros.

Linear combination
    of some set of vectors :math:`{ v^{1} , ... , v^{n} }` is given by multiplying each vector :math:`v^{i}` by a corresponding scalar coefficient and adding the results: :math:`\sum_{i}c_{i}v^{i}`.

Span
    of a set of vectors is the set of all points obtainable by linear combination of the original vectors.

A set of vectors is **linearly independent** if no vector in the set is a linear combination of the other vectors.

Only **square** matrix with linearly independent columns have **determinant**.  

A square matrix with linearly dependent columns is known as **singular**.

For square matrices the left inverse and right inverse are equal :math:`AA^{-1}=I`.

Norms
    are functions mapping vectors to non-negative values. Can be threated as size of the vector.

:math:`L^{p}` norm is given by :math:`||x||_{p}=(\sum_{i}|x_{i}|^{p})^{1/p}`, for :math:`p \in \mathbb{R}, p \geq 1`.

Euclidean norm
    the :math:`L^{2}` norm, with :math:`p = 2`.

Squared :math:`L^{2}` norm can be calculated simply as :math:`x^{T}x`.
