.. title: Main Formulas
.. slug: pt-main-formulas
.. date: 2017-08-17 08:08:13 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

**Some Axioms**

- :math:`P(A) + P(A^c) = 1`
- :math:`P(A \cup B) = P(A) + P(B) - P(A \cap B) = P(A) + P(A^c \cap B)`
- :math:`P(A \cup B) \leqslant P(A) + P(B)` - union bound
- :math:`P(A \cup B \cup C) = P(A) + P(A^c \cap B) + P(A^c \cap B^c \cap C)`

**From De Morgan’s laws**

- :math:`(S \cap T)^c = S^c \cup T^c`
- :math:`(S \cup T)^c = S^c \cap T^c`
- :math:`P(A \cap B) = 1 - P(A \cap B)^c = 1 - P(A)^c \cup P(B)^c = 1 - (1 - P(A)) \cup (1 - P(B))`

**Conditional Probability (probability of A given B)**

- :math:`P(A|B) = \frac{P(A \cap B)}{P(B)}` if :math:`P(B) > 0`
- :math:`P(A|B) \geqslant 0` assuming :math:`P(B) > 0`
- :math:`P(\Omega | B) = \frac{P(\Omega \cap B)}{P(B)} = 1`
- if :math:`A \cap C = \varnothing`, then :math:`P(A \cup C | B) = P(A|B) + P(C|B)`

Radar example:

- :math:`P(A \cap B) = P(A) * P(B|A)`
- :math:`P(B) = P(A \cap B) + P(A^c \cap B)`
- :math:`P(A|B) = \frac{P(A \cap B)}{P(B)}`
- :math:`P(A \cap B) = P(B) * P(A|B) = P(A) * P(B|A)`

**Total probability theorem:**

.. math::

  P(B) = \sum_{i}P(A_i) * P(B|A_i)

**Bayes' rule**

.. math::

  P(A_i | B) = \frac{P(A_i) * P(B | A_i)}{\sum_j P(A_j) * P(B | A_j)}

.. math::

  P(A|B) = \frac{P(A) * P(B|A)}{P(B)}

**Independence**

- :math:`P({A, B, C}) = P(A) + P(B) + P(C)`
- :math:`P(A \cap B) = P(A) * P(B)`
- :math:`P(A \cap B) = P(A)P(B|A) = P(B)P(A|B)`
- :math:`P(A|B) = P(A)`
- :math:`P(A \cap B^c) = P(A) P(B^c)`
- :math:`P(A^c \cap B^c) = P(A^c) P(B^c)`

**Conditional independence**

:math:`P(A \cap B | C) = P(A|C) * P(B |C)`

**Reliability**

:math:`P(A \cap B) = P(A) * P(B)`

Serial: :math:`P(a \rightarrow b) = p^k`

Parallel: :math:`P(a \rightarrow b) = 1 - (1 - p)^k`


**Conditional probability of smaller subset**

Given events :math:`C, D, E` such that:

- :math:`D \subset E`
- :math:`C \cap D = C \cap E`

than: :math:`P(C|D) \geq P(C|E)`
