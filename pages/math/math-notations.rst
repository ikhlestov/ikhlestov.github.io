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

- :math:`\in` - is member of
  
  - :math:`2 \in \{1, 2, 3, 4\}`

- :math:`\notin` - is not member of
  
  - :math:`2 \notin \{1, 3, 5\}`

- :math:`\emptyset` and :math:`\varnothing` or :math:`\{ \}` - empty set
- :math:`\cup` - union, everything in both sets
  
  - :math:`\{1, 2, 3\} \cup \{3, 4, 5\} = \{1, 2, 3, 4, 5\}`

- :math:`\cap` - intersection, only what is in common in both sets

  - :math:`\{1, 2, 3\} \cap \{2, 3, 4\} = \{2, 3\}`

- :math:`\subset` - subset of set

  - :math:`\{1, 2, 3\} \subset \{1, 2, 3, 4, 8\}`

- :math:`\supset` - superset of set

  - :math:`\{1, 2, 3, 4, 8\} \supset \{1, 2, 3\}`

- :math:`A'`, :math:`A^c`, :math:`\overline{\rm A}` - :math:`A` compliment, everything not in :math:`A`

.. image:: /images/math/math-notations/set_notations.jpg

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

Other
=====

:math:`[x]_{+} = max(0, x)`
