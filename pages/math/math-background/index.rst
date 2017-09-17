.. title: Math background
.. slug: math-background
.. date: 2017-08-24 08:58:24 UTC
.. tags: 
.. category: 
.. link: 
.. description:
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents

Sets
==============

Set a collection of distinct elements:

- :math:`{a, b, c, d}` - finite
- :math:`\mathbb{R}` : real numbers - infinite
- :math:`{x \in \mathbb{R}: cos(x) > 1/2}` - set with restriction

Notations:

- :math:`\Omega` - universal set(set that contain all objects)

- :math:`\in` - is member of
  
  - :math:`2 \in \{1, 2, 3, 4\}`

- :math:`\notin` - is not member of
  
  - :math:`2 \notin \{1, 3, 5\}`

- :math:`A'`, :math:`A^c`, :math:`\overline{\rm A}` - :math:`A` compliment, everything not in :math:`A`

  - :math:`x \in S^c if x \in \Omega, x \notin S`

- :math:`\emptyset` and :math:`\varnothing` or :math:`\{ \}` - empty set

  - :math:`\Omega^c = \emptyset`

- :math:`\cup` - union, everything in both sets
  
  - :math:`\{1, 2, 3\} \cup \{3, 4, 5\} = \{1, 2, 3, 4, 5\}`
  - :math:`x \in S \cup T \leftrightarrow x \in S \, \textsf{or} \> x \in T`
  - :math:`\cup_{n} S_{n}` - union of all :math:`n` sets

- :math:`\cap` - intersection, only what is in common in both sets

  - :math:`\{1, 2, 3\} \cap \{2, 3, 4\} = \{2, 3\}`
  - :math:`x \in S \cap T \leftrightarrow x \in S \, \textsf{and} \, x \in T`
  - :math:`\cap_{n} S_{n}` - intersection of all :math:`n` sets

- :math:`\subset` - subset of set

  - :math:`\{1, 2, 3\} \subset \{1, 2, 3, 4, 8\}`

- :math:`\supset` - superset of set

  - :math:`\{1, 2, 3, 4, 8\} \supset \{1, 2, 3\}`

.. image:: /images/math/math-notations/set_notations.jpg

Sets properties
----------------

- :math:`S \cup T = T \cup S`
- :math:`S \cap (T \cup U) = (S \cap T) \cup (S \cap U)`
- :math:`(S^c)^c = S`
- :math:`S \cup \Omega = \Omega`
- :math:`S \cap S^c = \emptyset`
- :math:`S \cap \Omega = S`
- :math:`S \cup (T \cup U) = (S \cup T) \cup U`
- :math:`S \cup (T \cap U) = (S \cup T) \cap (S \cup U)`

De Morgan's laws
----------------

- :math:`(S \cap T)^c = S^c \cup T^c`
- :math:`(\cap_{n} S_{n}^c) = \cup_{n} S_{n}^c`
- :math:`(S \cup T)^c = S^c \cap T^c`
- :math:`(\cup_n S_{n}^c) = \cap_n S_{n}^c`

Countable versus uncountable infinite sets
------------------------------------------

Countable: can be put in 1-1 correspondence with positive integers:

- Positive integers
- Integers: :math:`0, 1, -1, 2, -2, ...`
- Pairs of positive integers
- Rational numbers :math:`q`, with :math:`0 < q < 1`, :math:`1/2, 1/3, 2/3, 1/4, 2/4, ...`

Uncountable: not countable:

- The interval [0, 1]
- The reals
- The plane

Sequences ant their limits
===========================

Sequence is some collection of an elements:

- :math:`a_1, a_2, a_3, ...`
- sequence :math:`a_1`
- :math:`\{a_i\}`
- formal - function :math:`f: \mathbb{N} -> S, f(i) = a_i`

When does a sequence converge:

- If :math:`a_i \leq a_{i + 1}` for all :math:`i`, then either:

  - the sequence "converges to :math:`\infty`"
  - the sequence converges to some real number :math:`a`

- if :math:`|a_i - a| \leq b_i` for all :math:`i`, and :math:`b_i -> 0`, then :math:`a_i -> a`

Series
======

Infinite series
---------------

:math:`\sum_{i=1}^{\infty} a_i = \lim_{n -> \infty} \sum_{i=1}^n a_i` (provided limit exists)

- if :math:`a_i \geq 0`: limit exists
- if terms :math:`a_i` do not all have the same sign:

  - limit need not exist
  - limit may exist but be different if we sum in different order
  - **Fact**: limit exists and independent of order of summation if :math:`\sum_{i=1}^{\infty} |a_i| < \infty`

Order of summation in series
----------------------------

only if :math:`\sum |a_{ij}| < \infty`, then:

- :math:`\sum_{i \geq 1, j \geq 1} a_{ij} = \sum_{i=1}^{\infty}(\sum_{j = 1}^{\infty} a_{ij}) = \sum_{j=1}^{\infty}(\sum_{i = 1}^{\infty} a_{ij})`
- :math:`\sum_{(i, j) : j \leq i} a_{ij} = \sum_{i=1}^{\infty} \sum_{j=1}^{i} a_{ij} = \sum_{j=1}^{\infty} \sum_{i=j}^{\infty} a_{ij}`

Arithmetic progression
----------------------

.. math:: 

    a_{n}=a_{1}+(n-1)d
    
.. math:: 

    a_{n}=a_{m}+(n-m)d
    
.. math:: 

    S_n = \frac{n}{2}[2a_1 + (n - 1)d]
    
.. math:: 

    S_n = \frac{n}{2}[a_1 + a_n]
    
.. math:: 

    \overline{\rm n} = S_n / n
    
.. math:: 

    \overline{\rm n} = \frac{a_1 + a_n}{2}
    

where:

- :math:`a_1` is the first term of an arithmetic progression.
- :math:`a_n` is the nth term of an arithmetic progression.
- :math:`d` is the difference between terms of the arithmetic progression.
- :math:`n` is the number of terms in the arithmetic progression.
- :math:`S_n` is the sum of n terms in the arithmetic progression.
- :math:`\overline{\rm n}` is the mean value of arithmetic series.

Geometric progression
---------------------

.. math::
    
    a_n = ar^{n - 1}

.. math::

    a_n = ra_{n - 1}

.. math::

    S_n = \frac{a_1 (1 - r^n)}{1 - r}

.. math::

    S_n = \frac{a_1 - a_n * r}{1 - r}
  
    where r \ne 1

where:

- :math:`a` - initial value
- :math:`r` - common ratio

Simplified: :math:`S = \sum_{i=0}^{\inf} \alpha^i = 1 + \alpha + \alpha^2 + ... = \frac{1}{1 - \alpha}`, if :math:`|\alpha| < 1`


pass

Other
=====

If :math:`X` is a vector, and :math:`X \in \{-1, 1\}^{n}`, then :math:`X^{T}X == n`, where :math:`n` is a constant, and :math:`n == len(X)`.
