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
- 1x1 convolutions from `Network-in-network(NiN) <https://arxiv.org/abs/1312.4400>`__. With them we may reduce features > perform usual convolution > increase number of features
- Average pooling layer as part of the last classifier
- Inception module(parallel computation of various filter with 1x1 convs and after concatenating them)
- Flattened convolutions(Cx1, 1xC kernels)
- Bypassing features over two layers(as in ResNet)
- Concatenating features from current layer with features from previous ones(as in DenseNet)
- Inception V4 - combine ResNet features propagating approach with Inception module.
- Combine Inception Block with DenseNet approach.
- `Blog post <https://medium.com/towards-data-science/neural-network-architectures-156e5bad51ba#.itgibj8dm>`__ about various Neural Networks for image classification.
- `XCeption block <https://arxiv.org/pdf/1610.02357.pdf>`__ with separable convolutions(with or without ReLU after it).
- Depthwise separable convolution filters `initial paper <https://arxiv.org/pdf/1412.5474.pdf>`__
- LSTM or GRU cell
- attention mechanisms
- Various activation functions
- Max pooling or average pooling
- Use conv with stride without overlaping, not average/max pooling
- 1x1 convs and then separable by channels 3x3 convs
- Separable by channnels 3x3 convs and after 1x1 convs for all features

Optimization:

- Batch norm
- Regularization loss
- Various learning rate
- Dropout

Learning:

- Dataset augmentation
- Learn network to one image size(224x224) and fine tune after for less epochs to larger size(448x448 for example)
- Train image detection network with image classification dataset

A systematic evaluation of CNN modules:

- `Link to initial paper <https://arxiv.org/pdf/1606.02228.pdf>`__
- use ELU non-linearity without batchnorm or ReLU with it.
- apply a learned colorspace transformation of RGB.
- use the linear learning rate decay policy.
- use a sum of the average and max pooling layers.
- use mini-batch size around 128 or 256. If this is too big for your GPU, decrease the learning rate proportionally to the batch size.
- use fully-connected layers as convolutional and average the predictions for the final decision.
- when investing in increasing training set size, check if a plateau has not been reach.
- cleanliness of the data is more important then the size.
- if you cannot increase the input image size, reduce the stride in the con- sequent layers, it has roughly the same effect.
- if your network has a complex and highly optimized architecture, like e.g. GoogLeNet, be careful with modifications.
