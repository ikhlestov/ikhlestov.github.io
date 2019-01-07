.. title: Image classification and the data-driven approach, k-nearest neighbor
.. slug: 1_image_classification
.. date: 2016-12-15 21:55:43 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents:

Introduction
============

Challenges for image recognition:

- Viewpoint variation

- Scale variation

- Deformation

- Occlusion

- Illumination conditions

- Background clutter

- Intra-class variation


*Data-driven approach* means not build exact algorithm to separate a data, but provide a dataset with correct labels and learn and algorithm by example.

Nearest neighbor classifier
===========================

Images may be compared by **L1 distance**, where the sum is taken over all pixels.:

.. math::

    d_1(I_1, I_2) = \sum_p |I_1^p - I_2^p|

or with **L2 distance**, for example:

.. math::

    d_1(I_1, I_2) = \sqrt{\sum_p (|I_1^p - I_2^p|)^2}

In code simple classifier can be implemented as:

.. code-block:: python

    class NearestNeighbor:
        def train(self, data, labels):
            self.Xtr = data
            self.Ytr = labels

        def predict(self, X):
            """X array of images"""
            predictions = []
            for idx in range(X.shape[0]):
                # compute L1 distance
                distance = np.sum(np.abs(self.Xtr - X[idx, :]), axis=1)
                min_index = np.argmin(distances)
                prediction.append(self.Ytr[min_index])

            return np.array(predictions)

**L1 vs L2.** In particular, the L2 distance is much more unforgiving than the L1 distance when it comes to differences between two vectors.
That is, the L2 distance prefers many medium disagreements to one big one.

k-Nearest Neighbor Classifier
=============================

The same as nearest neighbor classifier, but instead of finding the single closest image in the training set, we will find the top **k** closest images, and have them vote on the label of the test image.

Cross validation
================

Cross validation means not freeze train and validation datasets, but split them on *k* folds and perform *k* runs with validation set to various split each run.
