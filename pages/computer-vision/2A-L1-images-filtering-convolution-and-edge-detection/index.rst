.. title: Images, filtering, convolution and edge detection
.. slug: 2A-L1-images-filtering-convolution-and-edge-detection
.. date: 2019-10-27 11:17:22 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents::

Images as a functions
======================

Images can be represented as a function:

.. figure:: /images/computer-vision/2A-L1/astronaut_gray_slice.png
    :alt: astronaut image
    :width: 300 px

.. figure:: /images/computer-vision/2A-L1/astronaut_slice_surface.png
    :alt: astronaut image surface
    :width: 300 px

We think of an image as a function, :math:`f` or :math:`I`, from :math:`\mathbb{R}^2` to :math:`\mathbb{R}`:

- :math:`f(x, y)` gives the intensity or value at position :math:`(x,y)`.

A color image is just three functions "stacked" together.
We can write this as "vector-valued function":

.. math::
    
    f(x, y) =
    \begin{bmatrix}
        r(x, y) \\\\
        g(x, y) \\\\
        b(x, y)
    \end{bmatrix}

In computers images are represented as a set of numbers, not continuous functions:

.. figure:: /images/computer-vision/2A-L1/image_one_computer.png
    :alt: Image representation in computers
    :width: 600px

In computer vision we typically operate on digital(discrete) images:

- *Sample* the 2D space on regular grid
- *Quantize* each sample (round to "nearest integer")

Noise
======

Noise is just another function that is combined with the original function to get a new one:

.. math::

    I'(x, y) = I(x, y) + \eta(x, y)


Types:

- **Impulse** (salt): random occurrences of white pixels
- **Pepper**: random black pixels
- **Salt and pepper**: random occurrences of black and white pixels
- **Gaussian noise**: variations in intensity drawn from a Gaussian normal distribution

.. figure:: /images/computer-vision/2A-L1/noises.png
    :alt: Example of different noises

To apply a noise it's enough just to add it to the initial image:

.. code-block:: python

    noise = np.random.normal(mean, variance ** 0.5, image.shape)
    output = image + noise

.. figure:: /images/computer-vision/2A-L1/applied_noise_example.png
    :alt: Example of applied noise

Effect of :math:`\sigma` (standard deviation) on Gaussian noise. Just to remind: :math:`variance = \sigma^2`.

.. figure:: /images/computer-vision/2A-L1/gaussian_noise.png
    :alt: Gaussian noise depends on sigma


Filtering
=========

