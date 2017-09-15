.. title: Math Notations
.. slug: math-notations
.. date: 2017-07-06 17:31:46 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents:

Sets notations
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

Sets properties:

- :math:`S \cup T = T \cup S`
- :math:`S \cap (T \cup U) = (S \cap T) \cup (S \cap U)`
- :math:`(S^c)^c = S`
- :math:`S \cup \Omega = \Omega`
- :math:`S \cap S^c = \emptyset`
- :math:`S \cap \Omega = S`
- :math:`S \cup (T \cup U) = (S \cup T) \cup U`
- :math:`S \cup (T \cap U) = (S \cup T) \cap (S \cup U)`

De Morgan's laws

- :math:`(S \cap T)^c = S^c \cup T^c`
- :math:`(\cap_{n} S_{n}^c) = \cup_{n} S_{n}^c`
- :math:`(S \cup T)^c = S^c \cap T^c`
- :math:`(\cup_n S_{n}^c) = \cap_n S_{n}^c`

Progressions
============

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

Other
=====

:math:`[x]_{+} = max(0, x)`
