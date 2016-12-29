.. title: RBM based Autoencoders with tensorflow
.. slug: rbm-based-autoencoders-with-tensorflow
.. date: 2016-12-28 20:33:15 UTC
.. tags: draft
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

**This is draft of post - feel free to comment/mail me about any errors**

Recently I try to implement RBM based autoencoder in tensorflow similar to RBMs described in `Semantic Hashing <http://www.cs.utoronto.ca/~rsalakhu/papers/semantic_final.pdf>`__ paper by Ruslan Salakhutdinov and Geoffrey Hinton. It seems that with RBM pretrained weights autoencoders should converge faster. So I've decide to check this.  

This post will describe some roadblocks for RBMs/autoencoders implementation in tensorflow and compare results of different approaches. I assume reader previous knowledge of tensorflow and machine learning field.

RBMs different from usual neural networks in some ways:

Neural networks usually perform weight update by Gradient Descent, but RMBs use **Contrastive Divergence** (which is basically a funky term for "approximate gradient descent" `link to read <http://deeplearning.net/tutorial/rbm.html>`__). At a glance contrastive divergence compute difference between **positive phase** (energy of first encoding) and **negative phase** (energy of last encoding).

.. code-block:: python

    positive_phase = tf.matmul(
        tf.transpose(visib_inputs_initial), first_encoded_probability)
    negative_phase = tf.matmul(
        tf.transpose(last_reconstructed_probability), last_encoded_probability)
    contrastive_divergence = positive_phase - negative_phase

Also key feature of RMB that it encode output in binary mode, not as probabilities. More about RMBs you may read `here <http://blog.echen.me/2011/07/18/introduction-to-restricted-boltzmann-machines/>`__ or `here <http://rocknrollnerd.github.io/ml/2015/07/18/general-boltzmann-machines.html>`__.

As prototype one layer tensorflow rbm `implementation <https://github.com/blackecho/Deep-Learning-TensorFlow/blob/master/yadlt/models/rbm_models/rbm.py>`__ was used. For testing I've take usual `MNIST <https://en.wikipedia.org/wiki/MNIST_database>`__ dataset(dataset of handwritten digits).

Many layers implementation
==========================

At first I've implement `multi layers RBM(Add link to code here) <fill_link>`__ with 3 layers. Because we not use usual tensorflow optimizers we may stop gradient for every variable with `tf.stop_gradient(variable_name)` and this will speed up computation a little bit. After construction two questions arised:
- Should every layer hidden units be binary encoded or only last one?
- Should we update every layer weights/biases at once per step, or first train only first two layers, after layers 2 and 3, and so on?

So I've run model with all binary units and only with last binary unit. And it seems that model with only last layer binarized trains better. After a while I note that this approach was already proposed in the paper, but I somehow miss this.

.. thumbnail:: /images/rbm-based-autoencoders-with-tensorflow/01_layers_binarization.png

    Errors with respect to steps

So let's stop with last layer binarized and try different train approaches. To build model that will train only pair of layers we need train two layers model, save it, build new model with one more layer, load pretrained first two layers weights/biases and continue train last two layers. During implementation I've meet some trouble - tensorflow have no method to initialize all not initialized previously variables method. Maybe I just didn't find this. So I've finish with approach when I directly send variable that should be restored and variables that should be initialized.

.. code-block:: python
    
    # restore previous variables
    restore_vars_dict = self._get_restored_variables_names()
    restorer = tf.train.Saver(restore_vars_dict)
    restorer.restore(sess, self.saves_path)

    # initialize not restored variables
    new_variables = self._get_new_variables_names()
    sess.run(tf.initialize_variables(new_variables))

After testing is seems that both training approaches converge to approximately same error. But some another cool stuff - model that was trained by pair lairs trains faster in time.

.. thumbnail:: /images/rbm-based-autoencoders-with-tensorflow/02_layers_training_error.png

    Errors with respect to steps

.. thumbnail:: /images/rbm-based-autoencoders-with-tensorflow/02_layers_training_relative.png

    Errors with respect to time consumption

So we stop with RBM trained with only last layer binarized and trained with *two layers only* strategy.

Build autoencoder from RBM
==========================

After get pretrained weights from RMB it's time to build autoencoder for fine tuning. To get encoding layer output as much as possible binarized as per paper advise we add Gaussian noise prior to layer. To simulate *deterministic noise* behavior, noise was generate for each input prior training and not changed during training. Also we want compare autoencoder loaded from RBM weights with self initialized usual autoencoder.

.. thumbnail:: /images/rbm-based-autoencoders-with-tensorflow/03_rbm_and_new_initialized_autoencoders.png

    RBM initialized autoencoder vs newly initialized autoencoder

It seems that RBM initialized autoencoder continue training, but newly initialized autoencoder with same architecture after a while stuck at some point.

.. thumbnail:: /images/rbm-based-autoencoders-with-tensorflow/03_rbm_initialized_autoencoder.png
    
    Only RBM based autoencoder training process, for clarity

TODO: Visualize distribution of probabilities that should be converted to

Validation
==========
To validate received embeddings I generate them for test and train sets and use two approaches:
- Train SVM with train set and measure accuracy on test set.
- With hamming distance or dot product find 10 most similar pictures/embeddings to provided one and check how many labels are the same to provided array label.


TODO:
Final testing of all embeddings variants
links to models
links to validation approaches
description of params
