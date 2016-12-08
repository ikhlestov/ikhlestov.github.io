.. title: ML Bookmarks
.. slug: ml-bookmarks
.. date: 2016-10-11 14:59:07 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

This is the list of some useful papers or resources with short explanation

Leaning Neural Nets by itself
=============================

+ `HYPER NETWORKS <https://arxiv.org/pdf/1609.09106v1.pdf>`__ This work explores hypernetworks:  an approach of using a small network, also known as a hypernetwork, to generate the weights for a larger network.

+ `AdaNet: Adaptive Structural Learning of Artificial Neural Networks <https://arxiv.org/pdf/1607.01097v1.pdf>`__  Our approach simultaneously and adaptively learns both the structure of the network as well as its weights.

+ `A Roadmap towards Machine Intelligence <https://arxiv.org/pdf/1511.08130v2.pdf>`__   In this paper, some fundamental properties that intelligent machines should have were proposed, focusing in particular on *communication* and *learning*.

RNN, seq2seq and all related
============================

+ `A Neural Transducer <https://arxiv.org/pdf/1511.04868v4.pdf>`__ Net than can generate predicition as more inputs arrives, without attention mechanism.

+ `Attention and Augmented Recurrent Neural Networks <http://distill.pub/2016/augmented-rnns/>`__ Explanation of various RNNs complex architectures.  

+ `Fully Character-Level Neural Machine Translation without Explicit Segmentation <https://arxiv.org/pdf/1610.03017v1.pdf>`__  model that maps a source character sequence to a target character sequence without any segmentation. (CNN + highway + biGRU)

+ `Phased LSTM: Accelerating Recurrent Network Training for Long or Event-based Sequences<https://arxiv.org/pdf/1610.09513v1.pdf>`__ LSTMs with additional time gate controlled by time step. This gate allow update *cell value* and *hidden output* only during an *"open"* phase.

CNNs
====

+ `Punctuation Prediction for Unsegmented Transcript Based on Word Vector <http://www.lrec-conf.org/proceedings/lrec2016/pdf/103_Paper.pdf>`__ CNN for inserting punctuation to the text.

Reinforcement Learning
======================

+ `Progressive Neural Networks <https://arxiv.org/pdf/1606.04671.pdf>`__  progressive networks approach immune to forgetting and can leverage prior knowledge via lateral connections to previously learned features.

+ `Reward Augmented Maximum Likelihood for Neural Structured Prediction <https://arxiv.org/pdf/1609.00150v1.pdf>`__ (`Short Summary <https://drive.google.com/file/d/0B3Rdm_P3VbRDVUQ4SVBRYW82dU0/view>`__)This paper presents a simple and computationally efficient approach to incorporate task reward into a  maximum likelihood framework. We establish a connection between the log-likelihood and regularized expected reward objectives, showing that at a zero temperature, they are approximately equivalent in  the vicinity of the  optimal solution.


Optimization Techniques
=======================

+ `RECURRENT NEURAL NETWORK REGULARIZATION <https://arxiv.org/pdf/1409.2329v5.pdf>`__

+ `Recurrent Dropout without Memory Loss <http://arxiv.org/pdf/1603.05118.pdf>`__

+ `Styles of Truncated Backpropagation <http://r2rt.com/styles-of-truncated-backpropagation.html>`__


Other Topics
============

+ `Highway Networks <http://people.idsia.ch/~rupesh/very_deep_learning/>`__ - list of papers, code, etc.
