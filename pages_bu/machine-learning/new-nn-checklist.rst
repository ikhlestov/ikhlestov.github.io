.. title: New NN Checklist
.. slug: new-nn-checklist
.. date: 2017-03-24 17:17:40 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

Checklist that should be considered when building new Neural Network:

- Define/validate your data
- Preprocess the data
- Split data on train/validation/test sets
- Make small network
- Validate gradient if it was manually coded
- Try to use pretrained weights
- Measure accuracy/ loss
- Calculate overall quantity of trainable parameters and memory consumption
- Use SGD as first approach without momentum. After give a try to Nesterov momentum and Adam optimizer.
- Try to overfit with small amount of data
- Validate data precise
- Add more metrics    
- There should be clear metric that allow you to compare networks with different params.
- Add regularization to loss. Compare it with cross-entropy loss
- Try to find optimal parameters with random search or grid search
- If optimal params exist on the edge of available range it is important to double check larger range
- Add some bells and whistles. Your network should work fine without them also
