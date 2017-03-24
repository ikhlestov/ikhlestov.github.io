.. title: Architecture vs. Optimization Approaches
.. slug: architecture_vs_optimization_approaches
.. date: 2017-03-24 17:32:32 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

On this page I will try distinguish various approaches that now used for building NN.
For example using convolution or LSTM is an architecture approach.
But using batch normalization or not - is optimization, because it can be added to any network without any architecture changes.

Architecture:

- Convs of with various kernels
- Concatenating features from current layer with features from previous ones(as in DenseNet)
- LSTM or GRU cell
- attention mechanisms

Optimization:

- Batch norm
- Regularization loss
- Various learning rate

Learning:

- Dataset augmentation
- Learn network to one image size(224x224) and fine tune after for less epochs to larger size(448x448 for example)
- Train image detection network with image classification dataset
