.. title: ML Bookmarks
.. slug: ml-bookmarks
.. date: 2016-10-11 14:59:07 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents::

RNN, seq2seq and all related
============================

+ `A Neural Transducer <https://arxiv.org/pdf/1511.04868v4.pdf>`__ Net than can generate predicition as more inputs arrives, without attention mechanism.

+ `Attention and Augmented Recurrent Neural Networks <http://distill.pub/2016/augmented-rnns/>`__ Explanation of various RNNs complex architectures.  

+ `Fully Character-Level Neural Machine Translation without Explicit Segmentation <https://arxiv.org/pdf/1610.03017v1.pdf>`__  model that maps a source character sequence to a target character sequence without any segmentation. (CNN + highway + biGRU)

+ `Phased LSTM: Accelerating Recurrent Network Training for Long or Event-based Sequences <https://arxiv.org/pdf/1610.09513v1.pdf>`__ LSTMs with additional time gate controlled by time step. This gate allow update *cell value* and *hidden output* only during an *"open"* phase.

+ `Search Results Words or Characters? Fine-grained Gating for Reading Comprehension <https://arxiv.org/pdf/1611.01724v1.pdf>`__

CNNs
====

+ `Punctuation Prediction for Unsegmented Transcript Based on Word Vector <http://www.lrec-conf.org/proceedings/lrec2016/pdf/103_Paper.pdf>`__ CNN for inserting punctuation to the text.
+ `DelugeNets: Deep Networks with Massive and Flexible Cross-layer Information Inflows <https://arxiv.org/pdf/1611.05552v4.pdf>`__
+ `Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization <https://arxiv.org/pdf/1610.02391.pdf>`__ (`git repo <https://github.com/ramprs/grad-cam>`__)
+ `Speed/accuracy trade-offs for modern convolutional object detectors <https://arxiv.org/abs/1611.10012>`__

LightWeight CNNs
----------------

+ `SqueezeNet <https://arxiv.org/abs/1602.07360>`__
+ `MobileNet <https://arxiv.org/abs/1704.04861>`__
+ `ShuffleNet <https://arxiv.org/abs/1707.01083>`__


Special Nets
============

One Shot Learning
-----------------

+ `Matching Networks for One Shot Learning <https://arxiv.org/pdf/1606.04080v1.pdf>`__ - one shot learning from Google Deep Mind for image net
+ `The More You Know: Using Knowledge Graphs for Image Classification <https://arxiv.org/pdf/1612.04844v1.pdf>`__
+ `Prototypical Networks for Few-shot Learning <https://arxiv.org/pdf/1703.05175.pdf>`__


Reinforcement Learning
----------------------

+ `Progressive Neural Networks <https://arxiv.org/pdf/1606.04671.pdf>`__  progressive networks approach immune to forgetting and can leverage prior knowledge via lateral connections to previously learned features.
+ `Reward Augmented Maximum Likelihood for Neural Structured Prediction <https://arxiv.org/pdf/1609.00150v1.pdf>`__ (`Short Summary <https://drive.google.com/file/d/0B3Rdm_P3VbRDVUQ4SVBRYW82dU0/view>`__)This paper presents a simple and computationally efficient approach to incorporate task reward into a  maximum likelihood framework. We establish a connection between the log-likelihood and regularized expected reward objectives, showing that at a zero temperature, they are approximately equivalent in  the vicinity of the  optimal solution.

Build Neural Nets with another Neural Nets
------------------------------------------

+ `HYPER NETWORKS <https://arxiv.org/pdf/1609.09106v1.pdf>`__ This work explores hypernetworks:  an approach of using a small network, also known as a hypernetwork, to generate the weights for a larger network.

+ `AdaNet: Adaptive Structural Learning of Artificial Neural Networks <https://arxiv.org/pdf/1607.01097v1.pdf>`__  Our approach simultaneously and adaptively learns both the structure of the network as well as its weights.

+ `A Roadmap towards Machine Intelligence <https://arxiv.org/pdf/1511.08130v2.pdf>`__   In this paper, some fundamental properties that intelligent machines should have were proposed, focusing in particular on *communication* and *learning*.

+ `Neural Architecture Search with Reinforcement Learning <https://openreview.net/pdf?id=r1Ue8Hcxg>`__ - broad grid search for availbale models architectures with LSTM. As result we receive new conv-net architecture and new RNN node.

Other Topics
------------

+ `Highway Networks <http://people.idsia.ch/~rupesh/very_deep_learning/>`__ - list of papers, code, etc.
+ `NIPS 2016 Tutorial: Generative Adversarial Network <https://arxiv.org/pdf/1701.00160v1.pdf>`__
+ Gumbel-Softmax at Categorical Variational Autoencoders - `blog post <http://blog.evjang.com/2016/11/tutorial-categorical-variational.html>`__. Categorical Reparameterization with Gumbel-Softmax `original paper <https://arxiv.org/pdf/1611.01144.pdf>`__
+ `Survey of resampling techniques for improving classification performance in unbalanced datasets <https://arxiv.org/pdf/1608.06048.pdf>`__
+ `Speed/accuracy trade-offs for modern convolutional object detectors <https://arxiv.org/abs/1611.10012>`__

Optimization Techniques
=======================

+ `RECURRENT NEURAL NETWORK REGULARIZATION <https://arxiv.org/pdf/1409.2329v5.pdf>`__

+ `Recurrent Dropout without Memory Loss <http://arxiv.org/pdf/1603.05118.pdf>`__

+ `Styles of Truncated Backpropagation <http://r2rt.com/styles-of-truncated-backpropagation.html>`__

+ `Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift <https://arxiv.org/pdf/1502.03167v3.pdf>`__

+ `Hyperparameter optimization for Neural Networks <http://neupy.com/2016/12/17/hyperparameter_optimization_for_neural_networks.html>`__ - example of many optimization approaches from NeuPy library.

Papers regarding efficient backprop and neural networks training
----------------------------------------------------------------

+ `Why Momentum Really Works <http://distill.pub/2017/momentum/>`__
+ `Stochastic Gradient Descent Tricks(Leon Bottou) <https://www.microsoft.com/en-us/research/wp-content/uploads/2012/01/tricks-2012.pdf>`__
+ `Efficient BackProb(Yann LeCun) <http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf>`__
+ `Practical Recommendations for Gradient-Based Training of Deep Architectures(Yoshua Bengio) <https://arxiv.org/pdf/1206.5533v2.pdf>`__
+ `FitNets: Hints for Thin Deep Nets <https://arxiv.org/pdf/1412.6550.pdf>`__
+ `Sobolev Training for Neural Networks <https://arxiv.org/pdf/1706.04859.pdf>`__ - training network with respect to optimize function derivatives.
+ `Set parameter for one network from another(Learning to learn by gradient descent by gradient descent) <https://arxiv.org/pdf/1606.04474.pdf>`__
+ `The Marginal Value of Adaptive Gradient Methods in Machine Learning <https://arxiv.org/abs/1705.08292>`__ - explanation why SGD can be better than Adam or other methods


Additional Resources
====================

+ `A Few Useful Things to Know about Machine Learning <http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf>`__ from cs231n course.


Benchmarks
----------

+ `DeepBench <https://github.com/baidu-research/DeepBench>`__ Benchmarking Deep Learning operations on different hardware

Datasets
--------

+ `e-Lab Video Data Set(s) <https://engineering.purdue.edu/elab/eVDS/>`__ Objects Tracking Dataset
