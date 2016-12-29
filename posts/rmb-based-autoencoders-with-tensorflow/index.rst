.. title: RMB based Autoencoders with tensorflow
.. slug: rmb-based-autoencoders-with-tensorflow
.. date: 2016-12-28 20:33:15 UTC
.. tags: draft
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

Recently I try to implement RBM based autoencoders in tesorflow similiar to RBMs described in `Semantic Hashing paper <http://www.cs.utoronto.ca/~rsalakhu/papers/semantic_final.pdf>`__ by Ruslan Salakhutdinov and Geoffrey Hinton. It seems that with RBM pretrained weights autoencoders can converge faster. So I've decide to check this.
RBM is different from usual neural networks in such was, that we perform weights updates not with usual Gradient Descent, but with **Contrastive Divergence**(which is basically a funky term for "approximate gradient descent").

Why use RBM based autoencoder(inspired by)
How RBM different from usual NN:
- Use Contrastive divergence
- Binarized

Use mnist as dataset
As prototype was used tf-rbm
Try to implement multy layers
Create all-at-once rbm
Should all layers be binarized or only last one?(last one)
Should all layers be trained at once or one by one.
Create one-to-one trained RBM
How to preload only part of weights?
See that one-to-one layers trains faster
Build autoencoder with preloaded weights
test autoencoder without preloaded weights
See how results are different
Final testing of all embeddings variants

Testing different embeddings:
Visually
bar plot
SVM
Accuracy by most similiar(haming distance and dot product)
