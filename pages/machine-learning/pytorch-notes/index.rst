.. title: PyTorch Notes
.. slug: pytorch-notes
.. date: 2017-07-17 17:14:51 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents::

PyTorch Fundamentals
====================

Simple array manipulations/creations
----------------------------------------

.. code-block:: python

    import torch

    # convert numpy array to pytorch array
    torch.Tensor(numpy_tensor)
    # or another way
    torch.from_numpy(numpy_tensor)

    # convert torch tensor to numpy representation
    pytorch_tensor.numpy()

    # create default arrays
    torch.ones((2, 2))
    torch.rand(2, 2)

Define manual seed
----------------------------------------

.. code-block:: python
    
    # CPU seed
    torch.manual_seed(42)

    # GPU seed
    torch.cuda.manual_seed_all(42)

Move from CPU to GPU and back
----------------------------------------

.. code-block:: python

    # move to GPU
    cpu_tensor.cuda()

    # move to CPU
    gpu_tensor.cpu()

Tensor manipulations
----------------------------------------

.. code-block:: python

    a = torch.rand(2, 3)

    # get the shape of tensor
    a.size()

    # reshape tensor to required shape
    a.view(3, -1)

    # simple addition
    b = torch.ones((2, 3))
    c = a + b
    c = torch.add(a, b)

    # in-place addition
    a.add_(b)

    # get the mean and std
    a.mean(dim=0)
    a.std(dim=1)

Variables and Gradients
=======================

Variable creation
----------------------------------------

.. code-block:: python

    import torch
    from torch.autograd import Variable

    # create variable
    a = Variable(torch.ones((2, 3)), requires_grad=True)

    # access variable tensor
    a.data

    # access variable gradient
    a.grad

Compute gradient
----------------------------------------

.. code-block:: python

    x = Variable(torch.ones(2), requires_grad=True)
    y = 5 * (x + 2) ** 2

    # backward should be called only on a scalar
    o = (1 / 2) * torch.sum(y)

    # compute backward
    o.backward()

    # now we have the gradients of x
    x.grad
    # 10, 10

Neural Networks
===============

Define simple NN
-----------------

Simple network without any optimizer and manually defined loss function

.. code-block:: python

    import torch
    from torch.autograd import Variable

    dtype = torch.FloatTensor
    N, D_in, H, D_out = 64, 1000, 100, 10

    x = Variable(torch.randn(N, D_in).type(dtype), requires_grad=False)
    y = Variable(torch.randn(N, D_out).type(dtype), requires_grad=False)

    w1 = Variable(torch.randn(D_in, H).type(dtype), requires_grad=True)
    w2 = Variable(torch.randn(H, D_out).type(dtype), requires_grad=True)

    learning_rate = 1e-6

    for t in range(500):

        y_pred = x.mm(w1)
        # simulate ReLU behavior
        y_pred = y_pred.clamp(min=0)
        y_pred = y_pred @ w2

        loss = (y_pred - y).pow(2).sum()
        # compute backward pass
        loss.backward()

        # manually apply the gradients
        w1.data -= learning_rate * w1.grad.data
        w2.data -= learning_rate * w2.grad.data

        # Manually zero the gradients after updating weights
        w1.grad.data.zero_()
        w2.grad.data.zero_()

NN with optimizer and loss
--------------------------

Now we will define network with ``nn`` module and with already predefined optimizer and loss

.. code-block:: python

    import torch
    from torch.autograd import Variable

    N, D_in, H, D_out = 64, 1000, 100, 10

    x = Variable(torch.randn(N, D_in))
    y = Variable(torch.randn(N, D_out), requires_grad=False)

    model = torch.nn.Sequential(
        torch.nn.Linear(D_in, H),
        torch.nn.ReLU(),
        torch.nn.Linear(H, D_out),
    )

    learning_rate = 1e-6
    loss_fn = torch.nn.MSELoss(size_average=False)
    optimizer = torch.nn.optim.SGD(model.parameters(), lr=learning_rate)

    for t in range(500):
        y_pred = model(x)
        loss = loss_fn(y_pred, target)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

NN class based
---------------

Create NN as class inherited from ``torch.nn.Module`` with convolution and linear layers

.. code-block:: python

    import torch
    import torch.nn.functional as F

    class Model(torch.nn.Module):
        def __init__(self, D_in, H, D_out):
            super().__init__()
            self.linear1 = torch.nn.Linear(D_in, H)
            self.linear2 = torch.nn.Linear(H, D_out)

        def forward(self, x):
            h_relu = F.relu(self.linear1(x))
            y_pred = self.linear2(h_relu)
            return y_pred


    N, D_in, H, D_out = 64, 1000, 100, 10

    x = Variable(torch.randn(N, D_in))
    y = Variable(torch.randn(N, D_out), requires_grad=False)

    model = Model(D_in, H, D_out)

    model = Model()
    criterion = torch.nn.MSELoss(size_average=False)
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)
    for t in range(500):
        y_pred = model(x)
        loss = criterion(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

Convolution Examples
--------------------

``Conv2d`` have such inputs: ``in_channels, out_channels, kernel_size``

.. code-block:: python

    import torch

    # Sequential based
    model = torch.nn.Sequential(
          torch.nn.Conv2d(1,20,5),
          torch.nn.ReLU(),
          torch.nn.Conv2d(20,64,5),
          torch.nn.ReLU()
        )

    # class based
    class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        return x

    model = Model()

Additional topics
==================

Train flag
----------

Train flag can be updated with boolean to disable dropout and batch norm learning

.. code-block:: python

    model.train(True)
    # execute train step
    model.train(False)
    # run inference step

Learning Rate Schedule
----------------------

PyTorch have a lot of learning rate schedulers `out of the box <http://pytorch.org/docs/master/optim.html#how-to-adjust-learning-rate>`__

.. code-block:: python

    # TODO: how they should be imported?

    scheduler = StepLR(optimizer, step_size=30, gamma=0.1)
    for epoch in range(100):
        scheduler.step()
        train()
        validate()

Data Loaders
------------

.. code-block:: python

    import pandas as pd
    import torch
    import torchvision as tv


    data_transforms = tv.transforms.Compose([
        tv.transforms.RandomCrop((64, 64), padding=4),
        tv.transforms.RandomHorizontalFlip(),
        tv.transforms.ToTensor(),
    ])


    class ImagesDataset(torch.utils.data.Dataset):
        def __init__(self, df, transform=None,
                     loader=tv.datasets.folder.default_loader):
            self.df = df
            self.transform = transform
            self.loader = loader

        def __getitem__(self, index):
            row = self.df.iloc[index]

            target = row['class_']
            path = row['path']
            img = self.loader(path)
            if self.transform is not None:
                img = self.transform(img)

            return img, target

        def __len__(self):
            n, _ = self.df.shape
            return n


    train_df = pd.read_csv('path/to/some.csv')
    train_dataset = ImagesDataset(
        df=train_df,
        transform=data_transforms['train'])

    train_loader = torch.utils.data.DataLoader(train_dataset,
                                               batch_size=10,
                                               shuffle=True,
                                               num_workers=16)

    # fetch the batch, same as `__getitem__` method
    for img, target in train_loader:
        pass

Use ``volatile`` flag during inference
---------------------------------------

In case of inference it's better provide ``volatile`` flag during variable creation. It can be provided only in case if you exactly sure that there will be no any gradients computing

.. code-block:: python

    input_ = torch.Variable(input_, volatile=True)

Weights initialization
----------------------

Weight initializtion in pytorch can be implemented in two ways:

.. code-block:: python

    import torch

    # as function call to `nn` module
    w = torch.Tensor(3, 5)
    torch.nn.init.xavier_normal(w)

    # as direct access to tensors data attribute
    def weights_init(m):
        classname = m.__class__.__name__
        if classname.find('Conv') != -1:
            m.weight.data.normal_(0.0, 0.02)
        elif classname.find('BatchNorm') != -1:
            m.weight.data.normal_(1.0, 0.02)
            m.bias.data.fill_(0)


    # for loop approach with direct access
    class MyModel(nn.Module):
        def __init__(self):
            for m in self.modules():
                if isinstance(m, nn.Conv2d):
                    n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                    m.weight.data.normal_(0, math.sqrt(2. / n))
                elif isinstance(m, nn.BatchNorm2d):
                    m.weight.data.fill_(1)
                    m.bias.data.zero_()
                elif isinstance(m, nn.Linear):
                    m.bias.data.zero_()

