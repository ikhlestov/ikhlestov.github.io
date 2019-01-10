.. title: Scikit-learn
.. slug: scikit-learn
.. date: 2016-06-21 23:46:34 UTC
.. tags: python, machine learning, ML, scikit-learn, sklearn
.. link:
.. description: List of usefull commands for pandas framework
.. author: Illarion Khlestov

.. contents:: Contents

Simple example
==============

.. code-block:: python

    # load the dataset
    from sklearn import datasets
    iris = datasets.load_iris()
    data_X = iris.data
    data_y = iris.target
    np.unique(iris_y)

    # initialize the Estimator
    estimator = Estimator(param1=1, param2=2)
    # get params of the existing estimator
    estimator.estimated_param_
    # train the estimator
    estimator.fit(data_X_train, data_y_train)
    # predict with estimator
    estimator.predict(data_X_test)
    # get estimator score - 1 is perfect prediction, 0 mean incorrect
    estimator.score(data_X_test, data_y_test)
    # The mean square error
    np.mean((estimator.predict(data_X_test) - data_y_test) ** 2)
    # get metrics for predictor
    from sklearn import metrics
    expected = digits.target[n_samples / 2:]
    predicted = classifier.predict(data[n_samples / 2:])
    print(metrics.classification_report(expected, predicted))

    # Choose best alpha based on score
    alphas = np.logspace(-4, -1, 6)
    regr = linear_model.Lasso()
    scores = [regr.set_params(alpha=alpha). \
                   fit(data_X_train, data_y_train). \
                   score(data_X_test, data_y_test) for alpha in alphas]
    best_alpha = alphas[scores.index(max(scores))]
    regr.alpha = best_alpha
    regr.fit(data_X_train, data_y_train)


KFolds
======

.. code-block:: python

    # to split data in train and test sets dynamically
    # compute score method of an estimator from kfolds
    # (total_number_of elements, numbers_of_folds)
    kfold = cross_validation.KFold(len(X_digits), n_folds=3)
    # kfold = [[train_indexes, test_indices], [train_indexes, test_indices], .. 3]
    [svc.fit(X_digits[train], y_digits[train]).score(X_digits[test], y_digits[test])
             for train, test in kfold]
    # cross_vall_score use folds to validate data
    cross_validation.cross_val_score(svc, X_digits, y_digits, cv=kfold, n_jobs=-1)

Support Vector Machines(SVMs)
=============================

.. code-block:: python

    #### description of regularization parameter C
    # Regularization is set by the C parameter: a small value for C means the
    # margin is calculated using many or all of the observations around the
    # separating line (more regularization);
    # a large value for C means the margin is calculated on observations
    # close to the separating line (less regularization).

    # choose C value based on best score
    # this is the same with the alpha above, but use 3 KFolds to find best param
    from sklearn import cross_validation, svm
    svc = svm.SVC(kernel='linear')
    C_s = np.logspace(-10, 0, 10)

    scores = list()
    scores_std = list()
    for C in C_s:
        svc.C = C
        # cv=3 - default for cross_val_score
        this_scores = cross_validation.cross_val_score(svc, X, y, n_jobs=1)
        scores.append(np.mean(this_scores))
        scores_std.append(np.std(this_scores))
    best_c = C_s[scores.index(max(scores))]
    svc.C = best_c
    svc.fit(data_X_train, data_y_train)

    # SVMs can be used in regression # –SVR (Support Vector Regression)–,
    # or in classification –SVC (Support Vector Classification).
    #### different types of SVC kernels
    # linear kernel
    svc = svm.SVC(kernel='linear')
    # polynomial kernel
    scv = svm.SVC(kernel='poly', degree=3)
    # RBF(Radial Basis Function) kernel
    scv = svm.SVC(kernel='rbf')


Grid Search
===========

.. code-block:: python

    # find the best param from the range with kfolds
    from sklearn.grid_search import GridSearchCV
    Cs = np.logspace(-6, -1, 10)
    clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)
    clf.fit(X_digits[:1000], y_digits[:1000])
    clf.best_score_
    clf.best_estimator_.C


    # Prediction performance on test set is not as good as on train set
    clf.score(X_digits[1000:], y_digits[1000:])


    # use existing cross validation model. Find parameters dinamically based on
    # estimator type. Note -CV at the end of estimator name
    from sklearn import linear_model, datasets
    lasso = linear_model.LassoCV()
    dataset = datasets.load_diabetes()
    X_data = dataset.data
    y_data = dataset.target
    lasso.fit(X_data, y_data)
    # The estimator chose automatically its lambda:
    lasso.alpha_


Unsupervised Learning
======================

.. code-block:: python

    # clustering
    from sklearn import cluster, datasets
    iris = datasets.load_iris()
    X_iris = iris.data
    y_iris = iris.target

    k_means = cluster.KMeans(n_clusters=3)
    k_means.fit(X_iris)

    print(k_means.labels_[::10])

    print(y_iris[::10])
