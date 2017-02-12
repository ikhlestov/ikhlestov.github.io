.. title: I.4.Numerical Computation
.. slug: i3numerical
.. date: 2017-01-08 14:06:13 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov


4.1 Overflow and underflow
==========================
Problems regarding rounding errors.
**Underﬂow** occurs when numbers near zero are rounded to zero.
**Overﬂow** occurs when numbers with large magnitude are approximated as :math:`\infty` or :math:`- \infty`.

4.2 Poor Conditioning
=====================
Conditioning refers to how rapidly a function changes with respect to small changes
in its inputs. Functions that change rapidly when their inputs are perturbed slightly
can be problematic for scientific computation because rounding errors in the inputs
can result in large changes in the output.

4.3 Gradient-Based Optimization
===============================

Optimization refers to the task of either minimizing or maximizing some function :math:`f (\boldsymbol{x})` by altering :math:`x`.

The function we want to minimize or maximize is called the **objective function** or **criterion**.
When we are minimizing it, we may also call it the **cost function**, **loss function** , or **error function**.

Value that minimizes or maximizes a function can be denoted with \*.
For example :math:`\boldsymbol{x}^{*} = \arg \min f(\boldsymbol{x})`

**Derivative** of some function :math:`y = f(x)` is denoted as :math:`f'(x)` or :math:`\frac{dy}{dx}`.
The derivative :math:`f'(x)` gives the slope of :math:`f(x)` at the point :math:`x`.
In other words, it specifies how to scale a small change in the input in order to obtain the corresponding change in the output: :math:`f(x + \epsilon) \approx f(x) + \epsilon f'(x)`

The derivative is useful for minimizing a function because it tells us how to change :math:`x` in order to make small improvement in :math:`y`.
We can thus reduce :math:`f (x)` by moving :math:`x` in small steps with opposite sign of the derivative. This technique is called **gradient descent** (first definition, second will be later).

When :math:`f'(x) = 0`, the derivative provides no information about which direction to move.
Points where :math:`f'(x) = 0` are known as **critical points** or **stationary points**.
Some critical points are neither maxima nor minima. These are known as **saddle points**.

A point that obtains the absolute lowest value of :math:`f (x)` is a **global minimum**.
It is possible for there to be only *one* global minimum or *multiple* global minima of the function.

We often minimize functions that have multiple inputs: :math:`f: \mathbb{R}^{n} \to \mathbb{R}`.
For the concept of "minimization" to make sense, there must still be only one (scalar) output.

For functions with multiple inputs, we must make use of the concept of **partial derivatives**.
The partial derivative :math:`\frac{\partial}{\partial x_{i}} f(x)` measures how :math:`f` changes **as only variable** :math:`x_{i}` increases at point :math:`\boldsymbol{x}`.
The **gradient** generalizes the notion of derivative to the case where the derivative is with respect to a vector:
the gradient of :math:`f` is the vector containing all of the partial derivatives, denoted
:math:`\nabla_{\boldsymbol{x}} f(\boldsymbol{x})`.
Element :math:`i` of the gradient is the partial derivative of :math:`f` with respect to :math:`x_i`. In multiple dimensions, critical points are points where every element of the gradient is equal to zero.

The **directional derivative** in direction :math:`\boldsymbol{u}` (a unit vector) is the slope of the function :math:`f` in direction :math:`u`.
In other words, the directional derivative is the derivative of the function
:math:`f(\boldsymbol{x} + \alpha \boldsymbol{u})` with respect to :math:`\alpha`, evaluated
at :math:`\alpha = 0`.
Using the chain rule, we can see that
:math:`\frac{\partial}{\partial\alpha} f(\boldsymbol{x} + \alpha \boldsymbol{u})`
evaluates to
:math:`\boldsymbol{u}^{T} \nabla_{\boldsymbol{x}} f(\boldsymbol{x})` when :math:`\alpha = 0`.

To minimize :math:`f`, we would like to find the direction in which :math:`f` decreases the fastest. We can do this using the directional derivative:

.. math::
    
    \min_{\boldsymbol{u}, \boldsymbol{u}^T \boldsymbol{u} = 1} \boldsymbol{u}^{T} \nabla_{\boldsymbol{x}} f(\boldsymbol{x})

    =     \min_{\boldsymbol{u}, \boldsymbol{u}^T \boldsymbol{u} = 1} ||\boldsymbol{u}||_2 ||\nabla_{\boldsymbol{x}} f(\boldsymbol{x})||_2 \cos \theta

where :math:`\theta` is the angel between :math:`\boldsymbol{u}` and the gradient.
Substituting in :math:`||\boldsymbol{u}||_2 = 1` and ignoring factors that do not depend on :math:`\boldsymbol{u}`, this simplifies to :math:`\min_{\boldsymbol{u}} \cos \theta`.
This is minimized when :math:`\boldsymbol{u}` points in the opposite direction as the gradient.
In other words, the gradient points directly uphill, and the negative gradient points directly downhill.
We can decrease :math:`f` by moving in the direction of the negative gradient.
This is known as the **method of steepest descent** or **gradient descent**.

Steepest descent proposes a new point

.. math::

    \boldsymbol{x'} = \boldsymbol{x} - \epsilon \nabla_{\boldsymbol{x}} f(\boldsymbol{x})

where :math:`\epsilon` is the **learning rate**, a positive scalar determining the size of the step.
We can set :math:`\epsilon` to a small constant.
Or evaluate :math:`f(\boldsymbol{x'} = \boldsymbol{x} - \epsilon \nabla_{\boldsymbol{x}} f(\boldsymbol{x}))` for several values of :math:`\epsilon` and choose the one that results in the smallest objective function value.
This last strategy is called a **line search**.

Steepest descent converges when every element of the gradient is zero (or, in practice, very close to zero). In some cases, we may be able to avoid running this iterative algorithm, and just jump directly to the critical point by solving the equation
:math:`\nabla_{\boldsymbol{x}} f(\boldsymbol{x}) = 0` for :math:`\boldsymbol{x}`.

Although gradient descent is limited to optimization in continuous spaces, the
general concept of repeatedly making a small move (that is approximately the best
small move) towards better configurations can be generalized to discrete spaces.
Ascending an objective function of discrete parameters is called **hill climbing**.
