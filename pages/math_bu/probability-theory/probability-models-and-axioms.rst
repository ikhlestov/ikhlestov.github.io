.. title: Probability Models and Axioms
.. slug: probability-models-and-axioms
.. date: 2017-08-17 08:08:13 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents::

.. |br| raw:: html

   <br />

Sample space
=============

- Describe possible outcomes
- Describe beliefs about likelihood outcomes

Possible outcomes:

- List (**set**) of possible outcomes, :math:`\Omega` (omega)
- List must be:
  
  - Mutually exclusive
  - Collectively exhaustive
  - All the "right" granularity

Interpretation and uses of probabilities:

- Measure frequency of the event
- Description of beliefs / betting performance

Sample space: discrete/finite example
---------------------------------------

.. figure:: /images/math/probability-theory/probability-models-and-axioms/01_discrete_example.png
    :width: 350
    :align: left

    Table description

.. figure:: /images/math/probability-theory/probability-models-and-axioms/02_discrete_example_seqential_descr.svg
    :width: 330
    :align: right

    Sequential description

|br|\ Two rolls of a tetrahedral die.

Sample space: continuous example
--------------------------------

:math:`(x, y)` such that :math:`0 \leqslant x, y \leqslant 1`

.. image:: /images/math/probability-theory/probability-models-and-axioms/03_continuous_example.png


Probability axioms
==================

Event
    is a subset of the sample space. Probability is assigned to events

.. image:: /images/math/probability-theory/probability-models-and-axioms/event.png
    :height: 150

Axioms:

- Nonnegativity: :math:`P(A) \geqslant 0`
- Normalization: :math:`P(\Omega) = 1`
- (Finite) Additivity: if :math:`A \cap B = \varnothing`, then :math:`P(A \cup B) = P(A) + P(B)`

Some simple consequences of the axioms:

- :math:`P(\varnothing) = 0`
- :math:`P(A) + P(A^c) = 1`
- if :math:`A_1, ..., A_k` disjoint, then :math:`P(A \cup ... \cup A_k) = \sum_{i=1}^{k}P(A_i)`
- :math:`P(\{S_1, S_2, ..., S_k\}) = P(\{S_1\} \cup \{S_2\} \cup ... \cup \{S_k\}) = P(\{S_1\}) + ... P(\{S_k\}) = P(S_1) + ... + P(S_k)`

More consequences of the axioms:

- if :math:`A \subset B`, then :math:`P(A) \leqslant P(B)` (img 1)
- :math:`P(A \cup B) = P(A) + P(B) - P(A \cap B) = P(A) + P(A^c \cap B)` (img 2)
- :math:`P(A \cup B) \leqslant P(A) + P(B)` - union bound
- :math:`P(A \cup B \cup C) = P(A) + P(A^c \cap B) + P(A^c \cap B^c \cap C)` (img 3)

.. image:: /images/math/probability-theory/probability-models-and-axioms/conseq_of_axioms.png
  :width: 600


Probability calculations
========================

Discrete finite example
-------------------------

Discrete uniform law:

- Assume :math:`\Omega` finite consist of :math:`n` equally likely elements
- Assume :math:`A` consist of :math:`k` elements, then

:math:`P(A) = k * frac{1}{n}`

.. TODO: add image 4

every outcome prob == :math:`\frac{1}{16}`

- :math:`P(X = 1) = 4 * \frac{1}{16}`
- let :math:`Z = min(X, Y)`

  - :math:`P(Z = 4) = 1/16`
  - :math:`P(Z = 2) = 5 * \frac{1}{16}`

.. TODO: add image 5

Discrete continuous example
----------------------------

Suppose we have :math:`(x, y)` such that :math:`0 \leq x, y, \leq 1`

Uniform probability law: Probability = Area

:math:`P(\{(x, y) | x + y \leq 1/2 \})` = triangle area = :math:`\frac{1}{2} * \frac{1}{2} * \frac{1}{2}`

:math:`P(\{0.5, 0.3 \})` = area of one point = :math:`0`

.. TODO: img 6

Probability calculations step
------------------------------

- Specify sample space
- Specify a probability law
- Identify an event of interest(if possible - graphical way)
- Calculate ...

Countable additivity
====================

Let's we have sample space :math:`\{1, 2, 3, ... \}`

:math:`P(n) = \frac{1}{2^n}, n=1, 2..`

:math:`\sum_{n=1}^{\infty} \frac{1}{2^n} = \frac{1}{2} \sum_{n=0}^{\infty} \frac{1}{2^n} = \frac{1}{2} * \frac{1}{1 - 1/2} = 1`

.. TODO: img 7

P(outcome is even) = :math:`P(\{2, 4, 6, ... \} ) = P(\{2\} \cup \{4\} \cup ..) = P(2) + P(4) + .. =`

:math:`= \frac{1}{2^2} + \frac{1}{2^4} + ... = \frac{1}{4}(1 + \frac{1}{4} + \frac{1}{4^2} + ...) = \frac{1}{4} * \frac{1}{1 - 1/4} = \frac{1}{3}`

Countable additivity axiom
--------------------------

Strengthens the finite additivity axiom:

- if :math:`A_1, A_2. A_3` is an finite sequence of disjoint events, then :math:`P(A_1 \cup A_2 \cup A_3 ...) = P(A_1) + P(A_2) + P(A_3)`
- additivity holds only for "countable" sequence of events
- the unit square(similarly the real line, etc.) is not countable. (It's elements cannot be arranged in a sequence)
- "Area" is a legitimate probability law on the unit square, as long as we do not try to assign probabilities/areas to "very strange" sets
