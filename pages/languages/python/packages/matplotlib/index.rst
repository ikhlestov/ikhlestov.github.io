.. title: Matplotlib
.. slug: matplotlib
.. date: 2016-10-12 23:51:12 UTC
.. tags: matplotlib
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov


Adjust default output size in jupyter notebook

.. code-block:: python

    pylab.rcParams['figure.figsize'] = (14,6)

Render different output at the same window

.. code-block:: python

    from IPython import display
    a = random.randn(2, 200)

    for i in range(3):
        a += 100
        pylab.scatter(*a)
        display.display(pylab.gcf())
        display.clear_output(wait=True)
        time.sleep(1.0)

Plot example

.. code-block:: python

    fig, axes = plt.subplots(nrows=8, ncols=1, figsize=(16, 4*len(corr_coeff)), sharey=True)
    axes[0].set_title('Correlation coefficients for ecolamp, samples_quantity=15', fontsize=20)
    pylab.title('Some name')
    for c in corr_coeff:
        ax1 = axes[counter]
        ax1.plot(c, label='some label')
        ax1.set_xlim(0, len(c))
        ax1.set_xlabel('time')
        ax1.set_ylabel('correlation')
        ax1.legend(loc='lowwer right')
        # handle the grid
        ax1.grid(True)
        ax1.xaxis.set_major_locator(locator)

Enable legend for all axes

.. code-block:: python

    _ = [axe.legend(loc='upper right') for axe in axes]
