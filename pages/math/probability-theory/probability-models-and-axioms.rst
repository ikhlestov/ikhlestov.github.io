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

Probability calculations
========================

pass

Countable additivity
====================

pass

