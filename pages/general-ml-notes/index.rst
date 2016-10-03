.. title: General ML Notes
.. slug: general-ml-notes
.. date: 2016-10-02 23:00:05 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

Sigmoid function: 

.. math::
    
    \sigma(z) = \frac{1}{1 + e^{-z}}
    
:math:`\sigma(\infty)\approx 1`, :math:`\sigma(-\infty)\approx 0`, 
but note, that :math:`\sigma(0)=1`  

Note: *sigmoid function* (:math:`\sigma`) == *logistic function*
so *sigmoid neurons* can be called as *logistic neurons*.
