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

Matrices
========

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

Vectors
=======

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
=====

Norms
    are functions mapping vectors to non-negative values. Can be threated as size of the vector.

:math:`L^{p}` norm is given by :math:`||x||_{p}=(\sum_{i}|x_{i}|^{p})^{1/p}`, for :math:`p \in \mathbb{R}, p \geq 1`.

Euclidean norm
    the :math:`L^{2}` norm, with :math:`p = 2`.

Squared :math:`L^{2}` norm can be calculated simply as :math:`x^{T}x`.


:math:`L^{2}` norm may be undesirable because it increases very slowly near the origin.
In these cases, we turn to a function that grows at the same rate in all locations, but retains mathematical simplicity: the :math:`L^{1}` norm.
The :math:`L^{1}` norm is commonly used in machine learning when the difference between zero and nonzero elements is very important.

:math:`L^{1}` norm
    :math:`||x||_{1}=\sum_i|x_{i}`

The :math:`L^{\infty}` norm, also known as the **max norm**. This norm simplifies to the absolute value of the element with the largest magnitude in the vector.

:math:`L^{\infty}` norm
    :math:`||x||_{\infty} = max_{i}|xi|`

Most common way to measure the size of a matrix this is **Frobenius norm** which is analogous to the :math:`L^{2}` norm of a vector.

Frobenius norm
    :math:`||A||_{F}=\sqrt{\sum_{i,j}A^{2}_{i,j}}`

The dot product of two vectors can be rewritten in terms of norms. 

Dot product
    :math:`x^{T}y=||x||_{2}||y||_{2}\cos\theta`

where :math:`\theta` is the angle between :math:`x` and :math:`y`.

Special Kinds of Matrices and Vectors
=====================================

**Diagonal** matrices consist mostly of zeros and have non-zero entries only alongthe main diagonal.
We write :math:`diag(v)` to denote a square diagonal matrix whose diagonal entries are given by the entries of the vector :math:`v`.
To compute :math:`diag(v)x`, we only need to scale each element :math:`x_i` by :math:`v_i`. In other words, :math:`diag(v)x = x \odot y`.
The inverse exists only if every diagonal entry is nonzero, and in that case, :math:`diag(v)^{-1} = diag([1/v_1, ..., 1/v_n]^T)`.

A **symmetric matrix** is any matrix that is equal to its own transpose: :math:`A = A^T`.

A **unit vector** is a vector with unit norm: :math:`||x||_2 = 1`.

A vector :math:`x` and a vector :math:`y` are **orthogonal** to each other if :math:`x^Ty = 0`.
In :math:`\mathbb{R}^{n}`, at most :math:`n` vectors may be mutually orthogonal with nonzero norm.
If the vectors are not only orthogonal but also have unit norm, we call them **orthonormal**.

An **orthogonal matrix** is a square matrix whose rows are mutually orthonormal and whose columns are mutually orthonormal: :math:`A^TA = AA^T = I`.
This implies that :math:`A^{-1} = A^T`.

Eigendecomposition
==================

calledeigen-decomposition, in which we decompose a matrix into a set of eigenvectors andeigenvalues.
Aneigenvectorof a square matrixAis a non-zero vectorvsuch that multi-plication by A alters only the scale of v:Av = λv.
The scalarλis known as theeigenvaluecorresponding to this eigenvector.
Ifvis an eigenvector ofA, then so is any rescaled vectorsvfors ∈ R, s = 0.Moreover,svstill has the same eigenvalue.

Suppose that a matrixAhasnlinearly independent eigenvectors,{v(1), . . . ,v(n)}, with corresponding eigenvalues{λ1, . . . , λn}. We may concatenate all of the
igenvectors to form a matrixVwith one eigenvector per column:V= [v(1), . . . ,v(n)]. Likewise, we can concatenate the eigenvalues to form a vectorλ= [λ1, . . . ,λn]. The eigendecomposition of A is then given byA = V diag(λ)V−1

every real symmetricmatrix can be decomposed into an expression using only real-valued eigenvectorsand eigenvalues:A = QΛQ, (2.41)whereQis an orthogonal matrix composed of eigenvectors ofA, andΛis adiagonal matrix. The eigenvalue Λi,iis associated with the eigenvector in columniofQ, denoted asQ:,i. BecauseQis an orthogonal matrix, we can think ofAasscaling space by λiin direction v(i).

While any real symmetric matrixAis guaranteed to have an eigendecomposi-tion, the eigendecomposition may not be unique. If any two or more eigenvectorsshare the same eigenvalue, then any set of orthogonal vectors lying in their spanare also eigenvectors with that eigenvalue, and we could equivalently choose aQusing those eigenvectors instead. By convention, we usually sort the entries ofΛin descending order. Under this convention, the eigendecomposition is unique onlyif all of the eigenvalues are unique.

The matrix is singular if and only if any of the eigenvalues are zero.The eigendecomposition of a real symmetric matrix can also be used to optimizequadratic expressions of the formf(x) =xAxsubject to||x||2= 1. Wheneverxis equal to an eigenvector ofA,ftakes on the value of the corresponding eigenvalue.The maximum value offwithin the constraint region is the maximum eigenvalueand its minimum value within the constraint region is the minimum eigenvalue.

A matrix whose eigenvalues are all positive is calledpositive deﬁnite. Amatrix whose eigenvalues are all positive or zero-valued is calledpositive semideﬁ-nite.
Positivesemideﬁnite matrices are interesting because they guarantee that∀x, xAx ≥0.Positive deﬁnite matrices additionally guarantee that xAx = 0 ⇒ x = 0.

Singular Value Decomposition
=============================

Thesingular value decomposition(SVD) provides another way to factorizea matrix, intosingular vectorsandsingular values.
Every real matrix has a singular valuedecomposition, but the same is not true of the eigenvalue decomposition.
Forexample, if a matrix is not square, the eigendecomposition is not deﬁned, and wemust use a singular value decomposition instead.

The singular value decomposition is similar, except this time we will writeAas a product of three matrices:A = U DV.

Suppose thatAis anm ×nmatrix. ThenUis deﬁned to be anm ×mmatrix,D to be an m × n matrix, and V to be an n ×n matrix
Each of these matrices is deﬁned to have a special structure. The matricesUandVare both deﬁned to be orthogonal matrices. The matrixDis deﬁned to bea diagonal matrix. Note that D is not necessarily square

The elements along the diagonal ofDare known as thesingular valuesofthe matrixA. The columns ofUare known as theleft-singular vectors. Thecolumns of V are known as as the right-singular vectors.
We can actually interpret the singular value decomposition ofAin terms ofthe eigendecomposition of functions ofA. The left-singular vectors ofAare theeigenvectors ofAA. The right-singular vectors ofAare the eigenvectors ofAA.The non-zero singular values ofAare the square roots of the eigenvalues ofAA.The same is true for AA.

Moore-Penrose pseudoinverse
===========================

Suppose we want to make a left-inverse :math:`B` of a matrix :math:`A`, so that we can solve a linear equation :math:`Ax = y` by left-multiplying each side to obtain :math:`x = By`.
Depending on the structure of the problem, it may not be possible to design a unique mapping from :math:`A` to :math:`B`.

If :math:`A` is taller than it is wide, then it is possible for this equation to have no solution. If :math:`A` is wider than it is tall, then there could be multiple possible solutions.
The pseudoinverse of :math:`A` is defined as a matrix

.. math::
    
    A^{+} = \lim_{\alpha\to 0} (A^TA + \alpha I)^{-1}A^T

Practical algorithms for computing the pseudoinverse are not based on this definition, but rather the formula

.. math::
    A^{+} = VD^{+}U^T

where :math:`U`, :math:`D` and :math:`V` are the singular value decomposition of :math:`A`, and the pseudoinverse :math:`D^{+}` of a diagonal matrix :math:`D` is obtained by taking the reciprocal of its non-zero elements then taking the transpose of the resulting matrix.

When :math:`A` has more columns than rows, then solving a linear equation using the pseudoinverse provides one of the many possible solutions. Specifically, it provides the solution :math:`x=A^{+}y` with minimal Euclidean norm :math:`||x||_2` among all possible solutions.

When :math:`A` has more rows than columns, it is possible for there to be no solution. In this case, using the pseudoinverse gives us the :math:`x` for which :math:`Ax` is as close as possible to :math:`y` in terms of Euclidean norm :math:`||Ax − y||_2`.

The Trace Operator
==================

Trace operator gives the sum of all of the diagonal entries of a matrix:

.. math::
    
    Tr(A) = \sum_i A_{i, i}


For example, the trace operator provides an alternative way of writing the Frobenius norm of a matrix:

.. math::

    ||A||_F=\sqrt{(Tr(AA^T))}

Also: :math:`Tr(A) = Tr(A^T)`, and :math:`Tr(ABC) = Tr(CAB) = Tr(BCA)`.

The Determinant
===============

The determinant of a square matrix, denoted :math:`det(A)`, is a function mapping matrices to real scalars.
The determinant is equal to the product of all the eigenvalues of the matrix. The absolute value of the determinant can be thought of as a measure of how much multiplication by the matrix expands or contracts space. If the determinant is 0, then space is contracted completely along at least one dimension, causing it to lose all of its volume. If the determinant is 1, then the transformation preserves volume.

