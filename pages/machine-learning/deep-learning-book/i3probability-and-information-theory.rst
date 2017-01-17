.. title: I.3.Probability And Information Theory
.. slug: i3probability-and-information-theory
.. date: 2017-01-08 14:06:13 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

In many cases, it is more practical to use a simple but uncertain rule rather than a complex but certain one, even if the true rule is deterministic and our modeling system has the fidelity to accommodate a complex rule.

When we say that an outcome has a probability :math:`p` of occurring, it means that if we repeated the experiment infinitely many times, then proportion :math:`p` of the repetitions would result in that outcome.

This kind of reasoning does not seem immediately applicable to propositions that are not repeatable. For that cases we use **degree of belief**, with 1 indicating absolute certainty that the patient has the flu and 0 indicating absolute certainty that the patient does not have the flu.

So if we have a probability related directly to the rates at which events occur, this probability known as **frequentist probability** (deal the cards).

If probability related to qualitative levels of certainty, it's known as **Bayesian probability** (have patient flue or not).


Random Variables
================

A **random variable** is a variable that can take on different values randomly. On its own, a random variable is just a description of the states that are possible; it must be coupled with a probability distribution that specifies how likely each of these states are.

Random variables may be discrete or continuous. A discrete random variable is one that has a finite or countably infinite number of states. Note that these states are not necessarily the integers; they can also just be named states that are not considered to have any numerical value. A continuous random variable is associated with a real value.

Probability Distributions
=========================

A **probability distribution** is a description of how likely a random variable or set of random variables is to take on each of its possible states. The way we describe probability distributions depends on whether the variables are discrete or continuous.


Discrete Variables and Probability Mass Functions
=================================================

A probability distribution over discrete variables may be described using a **probability mass function (PMF)** (denoted as :math:`P`). :math:`P(x)` usually is not the same as :math:`P(y)`. The probability mass function maps from a state of a random variable to the probability of that random variable taking on that state.  Sometimes we define a variable first, then use :math:`\sim` notation to specify which distribution it follows later: :math:`\mathsf{x} \sim P(\mathsf{x})`.

Probability mass functions can act on many variables at the same time. Such a probability distribution over many variables is known as a **joint probability distribution**. :math:`P(\mathsf{x}=x, \mathsf{y}=y)` denotes the probability that :math:`\mathsf{x}=x` and :math:`\mathsf{y}=y` **simultaneously**. We may also write :math:`P(x, y)` for brevity.

A function :math:`P` should satisfy the following properties:

- The domain of :math:`P` must be the set of all possible states of :math:`\mathsf{x}`.
- :math:`\forall x \in \mathsf{x}, 0 \leq P(x) \leq 1`
- :math:`\sum_{x \in \mathsf{x}} P(x) = 1`


Continuous Variables and Probability Density Functions
======================================================

When working with continuous random variables, we describe probability distributions using a **probability density function (PDF)** (denoted as :math:`p`).

:math:`p` must satisfy the following properties:

- The domain of :math:`P` must be the set of all possible states of :math:`\mathsf{x}`.
- :math:`\forall x \in \mathsf{x}, p(x) \geq 0`. Note that we do not require :math:`p(x) \leq 1`.
- :math:`\int p(x)d(x) = 1`.

A probability density function :math:`p(x)` does not give the probability of a specific state directly, instead the probability of landing inside an infinitesimal region with volume :math:`\delta x` is given by :math:`p(x)\delta x`.

We often denote that :math:`x` follows the uniform distribution on :math:`[a, b]` by writing :math:`x \sim U(a, b)` or :math:`u(x; a, b)`.


Marginal Probability
====================

**Marginal probability** - the probability distribution over the subset is known.

Suppose we know :math:`P(x, y)`. We can find :math:`P(x)` with the **sum rule**: :math:`\forall x \in \mathsf{x}, P(x) = \sum_{y} P(x, y)`.

When the values of :math:`P(x, y)` are written in a grid with different values of :math:`x` in rows and different values of :math:`y` in columns, it is natural to sum across a row of the grid, then write :math:`P(x)` in the margin of the paper just to the right of the row.

For continuous variables, we need to use integration instead of summation: :math:`p(x) = \int p(x, y)dy`

Conditional Probability
=======================

**Conditional probability** -  probability of some event, given that some other event has happened. We denote the conditional probability that :math:`\mathsf{y}=y` given :math:`\mathsf{x}=x`as :math:`P(\mathsf{y}=y | \mathsf{x}=x)` or just :math:`P(y| x)` - event :math:`y` occur depends on event :math:`x`. This probability can be computed as:

.. math::

    P(\mathsf{y}=y | \mathsf{x}=x) = \frac{P(\mathsf{y}=y, \mathsf{x}=x)}{P\mathsf{x}=x}

Computing the consequences of an action is called making an **intervention query**. Intervention queries are the domain of **causal modeling** (out of the scope of this book).

The Chain Rule of Conditional Probabilities
===========================================

Any joint probability distribution over many random variables may be decomposed into conditional distributions over only one variable:

.. math::

    P(x^{(1)}, ..., x^{(n)}) = P(x^{(1)}) \prod_{i=2}^{n} P(x^{i}| x^{(1)}, ..., x^{(i - 1)})

This observation is known as the **chain rule** or **product rule** of probability. For example:

.. math::

    P(a, b, c) = P(a|b, c)P(b, c)

    P(b, c) = P(b|c)P(c)

    P(a, b, c) = P(a|b, c)P(b|c)P(c)

Independence and Conditional Independence
=========================================

Two random variables :math:`x` and :math:`y` are **independent** if their probability distribution can be expressed as a product of two factors, one involving only :math:`x` and one involving only :math:`y`:

.. math::
    \forall x \in \mathsf{x}, y \in \mathsf{y}, p(\mathsf{x} = x, \mathsf{y} = y) = p(\mathsf{x} = x)p(\mathsf{y} = y) 

Two random variables :math:`x` and :math:`y` are **conditionally independent** given a random variable :math:`z` if the conditional probability distribution over :math:`x` and :math:`y` factorizes in this way for every value of :math:`z`:

.. math::
    \forall x \in \mathsf{x}, y \in \mathsf{y}, z \in \mathsf{z}, p(\mathsf{x} = x, \mathsf{y} = y | \mathsf{z} = z) = p(\mathsf{x} = x | \mathsf{z} = z)p(\mathsf{y} = y | \mathsf{z} = z) 


We can denote independence and conditional independence with compact notation: :math:`x \bot y` means that :math:`x` and :math:`y` are independent, while :math:`x \bot y | z` means that :math:`x` and :math:`y` are conditionally independent given :math:`z`.


Expectation, Variance and Covariance
====================================

The **expectation** or **expected value** of some function :math:`f(x)` with respect to a probability distribution :math:`P(x)` is the average or mean value that :math:`f` takes on when :math:`x` is drawn from :math:`P`. For discrete variables this can be computed with a summation:

.. math::
    
    \mathbb{E}_{x \sim P}[f(x)] = \sum_{x} P(x)f(x)

while for continuous variables, it is computed with an integral:

.. math::

    \mathbb{E}_{x \sim p}[f(x)] = \int p(x)f(x)dx.

By default, we can assume that :math:`\mathbb{E}[\cdot]` averages over the values of all the random variables inside the brackets. Likewise, when there is no ambiguity, we may omit the square brackets.

Expectations are linear, for example, :math:`\mathbb{E}_{x}[\alpha f(x) + \beta g(x)] = \alpha \mathbb{E}_{x}[f(x)] + \beta \mathbb{E}_{x}[g(x)]` when :math:`\alpha` and :math:`\beta` not dependent on :math:`x`.

The **variance** gives a measure of how much the values of a function of a random variable :math:`\mathsf{x}` vary as we sample different values of :math:`x` from its probability distribution:

.. math::

    Var(f(x)) = \mathbb{E}[(f(x) - \mathbb{E}[f(x)])^2]

When the variance is low, the values of :math:`f(x)` cluster near their expected value. The square root of the variance is known as the **standard deviation**.

The **covariance** gives some sense of how much two values are linearly related to each other, as well as the scale of these variables:

.. math::
    
    Cov(f(x), g(y)) = \mathbb{E}[(f(x) - \mathbb{E}[f(x)]) (g(y) - \mathbb{E}[g(y)])]


High absolute values of the covariance mean that the values change very much and are both far from their respective means at the same time. If the sign of the covariance is positive, then both variables tend to take on relatively high values simultaneously. If the sign of the covariance is negative, then one variable tends to take on a relatively high value at the times that the other takes on a relatively low value and vice versa. Other measures such as **correlation** normalize the contribution of each variable in order to measure only how much the variables are related, rather than also being affected by the scale of the separate variables

The notions of covariance and dependence are related, but are in fact distinct concepts. They are related because two variables that are independent have zero covariance, and two variables that have non-zero covariance are dependent. However, independence is a distinct property from covariance. For two variables to have zero covariance, there must be no linear dependence between them. Independence is a stronger requirement than zero covariance, because independence also excludes nonlinear relationships. It is possible for two variables to be dependent but have zero covariance.
For example, suppose we first sample a real number :math:`x` from a uniform distribution over the interval :math:`[−1,1]`. We next sample a random variable :math:`s`. With probability :math:`\frac{1}{2}`, we choose the value of :math:`s` to be 1. Otherwise, we choose the value of :math:`s` to be −1. We can then generate a random variable :math:`y` by assigning :math:`y=sx`. Clearly, :math:`x` and :math:`y` are not independent, because :math:`x` completely determines the magnitude of :math:`y`. However, :math:`Cov(x, y) = 0`.

The **covariance matrix** of a random vector :math:`\textbf{x} \in \mathbb{R}^{n}` is an :math:`n \times n` matrix, such that 

.. math::

    Cov(\textbf{x})_{i,j}= Cov(\mathsf{x}_i, \mathsf{x}_j).

The diagonal elements of the covariance give the variance:

.. math::
    
    Cov(\mathsf{x}_i, \mathsf{x}_i) = Var(\mathsf{x}_i).


Common Probability Distributions
================================

Bernoulli Distribution
----------------------

The **Bernoulli** distribution is a distribution over a single binary random variable.It is controlled by a single parameter :math:`\phi \in [0,1]`, which gives the probability of the random variable being equal to 1. It has the following properties:

.. math::

    P(\mathsf{x} = 1) = \phi

    P(\mathsf{x} = 0) = 1 - \phi

    P(\mathsf{x} = x) = \phi^{x}(1 - \phi)^{1 - x}

    \mathbb{E}_{\mathsf{x}}[\mathsf{x}] = \phi

    Var_{\mathsf{x}}(\mathsf{x}) = \phi(1 - \phi)


Multinoulli Distribution
------------------------

The **multinoulli** or **categorical** distribution is a distribution over a single discrete variable with :math:`k` different states, where :math:`k` is finite.
The multinoulli distribution is parametrized by a vector :math:`p \in [0,1]^{k−1}`, where :math:`p_i` gives the probability of the *i*-th state.
The final, *k*-th state’s probability is given by :math:`1− \mathsf{1}^T p`.Note that we must constrain :math:`\mathsf{1}^T p \leq 1`.
Multinoulli distributions are often used to refer to distributions over categories of objects, so we do not usually assume that state 1 has numerical value 1, etc.
For this reason, we do not usually need to compute the expectation or variance of multinoulli-distributed random variables.


Gaussian Distribution
---------------------

The most commonly used distribution over real numbers is the **normal distribution**, also known as the **Gaussian distribution**:

.. math::

    N(x; \mu, \sigma^{2}) = \sqrt{\frac{1}{2\pi \sigma^{2}}} \exp(-\frac{1}{2\sigma^2}(x - \mu)^2)

The two parameters :math:`\mu \in \mathbb{R}` and :math:`\sigma \in (0, \infty)` control the normal distribution.
The parameter :math:`\mu` gives the coordinate of the central peak.
This is also the mean of the distribution: :math:`\mathbb{E}[x] = \mu`.
The standard deviation of the distribution is given by :math:`\sigma`, and the variance by :math:`\sigma^{2}`.

When we evaluate the PDF, we need to square and invert :math:`\sigma`.
When we need to frequently evaluate the PDF with different parameter values, a more efficient way of parametrizing the distribution is to use a parameter :math:`\beta \in (0, \infty)` to control the precision or inverse variance of the distribution:

.. math::

    N(x; \mu, \beta^{-1}) = \sqrt{\frac{\beta}{2\pi }} \exp(-\frac{1}{2}\beta (x - \mu)^2)

The normal distribution generalizes to :math:`\mathbb{R}^n`, in which case it is known as the **multivariate normal distribution**.
It may be parametrized with a positive definite symmetric matrix :math:`\boldsymbol{\Sigma}`:

.. math::
    
    N(\boldsymbol{x}; \boldsymbol{\mu}, \boldsymbol{\Sigma}) = \sqrt{\frac{1}{(2\pi)^n det(\boldsymbol{\Sigma})}} \exp(-\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\boldsymbol{x} - \boldsymbol{\mu}))

The parameter :math:`\boldsymbol{\mu}` still gives the mean of the distribution, though now it is vector-valued.
The parameter :math:`\boldsymbol{\Sigma}` gives the covariance matrix of the distribution.
As in the univariate case, when we wish to evaluate the PDF several times for many different values of the parameters,
the covariance is not a computationally efficient way to parametrize the distribution, since we need to invert :math:`\boldsymbol{\Sigma}` to evaluate the PDF.
We can instead use a **precision matrix** :math:`\boldsymbol{\beta}`:


.. math::

    N(\boldsymbol{x}; \boldsymbol{\mu}, \boldsymbol{\beta}) = \sqrt{\frac{det(\boldsymbol{\beta})}{(2\pi)^n }} \exp(-\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^T \boldsymbol{\beta} (\boldsymbol{x} - \boldsymbol{\mu}))


We often fix the covariance matrix to be a diagonal matrix.
An even simpler version is the **isotropic** Gaussian distribution, whose covariance matrix is a scalar times the identity matrix.

Exponential and Laplace Distributions
-------------------------------------

**Exponential distribution** - a probability distribution with a sharp point at :math:`x= 0`:

.. math::

    p(x; \lambda) = \lambda \boldsymbol{1}_{x \geq 0} \exp(-\lambda x)

The exponential distribution uses the indicator function :math:`\boldsymbol{1}_{x \geq 0}` to assign probability zero to all negative values of :math:`x`.

A closely related probability distribution that allows us to place a sharp peak of probability mass at an arbitrary point :math:`\mu` is the **Laplace distribution**:

.. math::

    \textrm{Laplace}(x; \mu, \gamma) = \frac{1}{2\gamma} \exp(-\frac{|x - \mu|}{\gamma})

The Dirac Distribution and Empirical Distribution
-------------------------------------------------

In some cases, we wish to specify that all of the mass in a probability distribution clusters around a single point. This can be accomplished by defining a PDF using the Dirac delta function, :math:`\delta (x)`:

.. math::

    p(x) = \delta (x - \mu)

The Dirac delta function is defined such that it is zero-valued everywhere except 0, yet integrates to 1.
Dirac function is called a **generalized function** that is defined in terms of its properties when integrated.
We can think of the Dirac delta function as being thelimit point of a series of functions that put less and less mass on all points other than zero.

By defining :math:`p(x)` to be :math:`\delta` shifted by :math:`- \mu` we obtain an infinitely narrow and infinitely high peak of probability mass where :math:`x = \mu`.

A common use of the Dirac delta distribution is as a component of an **empirical distribution**:

.. math::

    \hat{p}(\boldsymbol{x}) = \frac{1}{x}\sum_{i=1}^{m} \delta (\boldsymbol{x} - \boldsymbol{x}^i)

which puts probability mass :math:`\frac{1}{m}` on each of the :math:`m` points :math:`\boldsymbol{x}^{(1)}, ..., \boldsymbol{x}^{(m)}` forming a given dataset or collection of samples.

The Dirac delta distribution is only necessary to define the empirical distribution over continuous variables.
For discrete variables,the situation is simpler: an empirical distribution can be conceptualized as a multinoulli distribution, with a probability associated to each possible input value that is simply equal to the **empirical frequency** of that value in the training set.

Mixtures of Distributions
-------------------------

One common way of combining distributions is to construct a **mixture distribution**.
A mixture distribution is made up of several component distributions.
On each trial, the choice of which component distribution generates the sample is determined by sampling a component identity from a multinoulli distribution:

.. math::

    P(\mathrm{x}) = \sum_{i} P(\mathrm{c} = i)P(\mathrm{x} | \mathrm{c} = i)

where :math:`P(\mathrm{c})` is the multinoulli distribution over component identities.

A **latent variable** is a random variable that we cannot observe directly.
The component identity variable :math:`\mathrm{c}` of the mixture model provides an example.
Latent variables may be related to :math:`\mathrm{x}` through the joint distribution, in this case, :math:`P(\mathrm{x}, \mathrm{c}) = P(\mathrm{x} | \mathrm{c})P(\mathrm{c})`.
The distribution :math:`P(\mathrm{c})` over the latent variable and the distribution :math:`P(\mathrm{x} | \mathrm{c})` relating the latent variables to the visible variables determines the shape of the distribution :math:`P(\mathrm{x})` even though it is possible to describe :math:`P(\mathrm{x})` without reference to the latent variable.

A very powerful and common type of mixture model is the **Gaussian mixture** model, in which the components :math:`p(\boldsymbol{x} | c=i)` are Gaussians.
Each component has a separately parametrized mean :math:`\boldsymbol{\mu}^{(i)}`and covariance :math:`\boldsymbol{\Sigma}^{(i)}`.
Some mixtures can have more constraints.
For example, the covariances could be shared across components via the constraint :math:`\boldsymbol{\Sigma}^{(i)} = \boldsymbol{\Sigma} \forall i`.
As with a single Gaussian distribution, the mixture of Gaussians might constrain the covariance matrix for each component to be diagonal or isotropic.

In addition to the means and covariances, the parameters of a Gaussian mixture specify the **prior probability** :math:`\alpha_{i} = P(\mathrm{c} = i)` given to each component :math:`i`.
The word "prior" indicates that it expresses the model’s beliefs about :math:`\mathrm{c}` *before* it has observed :math:`\boldsymbol{x}`.
By comparison, :math:`P(\mathrm{c} | \boldsymbol{x})` is a **posterior probability**, because it is computed *after* observation of :math:`\boldsymbol{x}`.
A Gaussian mixture model is a **universal approximator** of densities, in the sense that any smooth density can be approximated with any specific, non-zero amount of error by a Gaussian mixture model with enough components


Useful Properties of Common Functions
=====================================

**logistic sigmoid**

.. math::
    
    \sigma (x) = \frac{1}{1 + \exp (-x)}

Logistic sigmoid is commonly used to produce the :math:`\phi` parameter of a Bernoulli distribution because its range is :math:`(0,1)`.
The sigmoid function **saturates** when its argument is very positive or very negative, meaning that the function becomes very flat and insensitive to small changes in its input. See figure 1.

.. thumbnail:: /images/ML_notes/deep_learning_book/01_sigmoid_distribution.png

    Figure 1.

Another common function is the **softplus**

.. math::

    \zeta (x) = \log (1 + \exp (x))

The softplus function can be useful for producing the :math:`\beta` or :math:`\sigma` parameter of a normal distribution because its range is :math:`(0 , \infty)`.

Common properties to memorize:

.. math::

    \sigma (x) = \frac{\exp (x)}{\exp(x) + \exp(0)}

    \frac{d}{dx}\sigma(x) = \sigma(x)(1 - \sigma(x))

    1 - \sigma(x) = \sigma(-x)

    \log\sigma(x) = -\zeta(-x)

    \frac{d}{dx}\zeta(x) = \sigma(x)

    \forall x \in (0, 1), \sigma^{-1}(x) = \log(\frac{x}{1 - x})

    \forall x > 0, \zeta^{-1}(x) = \log(\exp(x) - 1)

    \zeta(x) = \int_{-\infty}^{x} \sigma(y)dy

    \zeta(x) - \zeta(-x) = x


Bayes' Rule
===========

Compute :math:`P(\mathrm{x} | \mathrm{y})` from :math:`P(\mathrm{y} | \mathrm{x})` if we know :math:`P(\mathrm{x})`:

.. math::

    P(\mathrm{x} | \mathrm{y}) = \frac{P(\mathrm{x}) P(\mathrm {y}| \mathrm{x})}{P(\mathrm{y})}

also :math:`P(\mathrm{y})` can be computed as :math:`P(\mathrm{x}) = \sum_{x} P(\mathrm{y} | \mathrm{x}) P(\mathrm{x})`


Technical Details of Continuous Variables
=========================================
Based on **measure theory**
