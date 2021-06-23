## TensorFlow Example 1
This demo use Keras to calculate a regression, i.e., find the best line of fit for a paired data set.
(While using neural networks and gradient descent is overkill for this kind of problem, it does make for a very easy to understand example.)

You're going to use TensorBoard to observe how training and test loss change across epochs. Hopefully, you'll see training and test loss decrease over time and then remain steady.

First, generate 1000 data points roughly along the line y = 0.5x + 2. Split these data points into training and test sets. Your hope is that the neural net learns this relationship.
### Run example 1
```
/home/test/.local/bin/jupyter-lab training.py
```
### Result


<img src="./example1/loss-1-before.png" width="300">

<img src="./example1/loss-1-after.png" width="300">


### Issues
```

```
### References
  * https://www.tensorflow.org/tensorboard/scalars_and_keras

## TensorFlow Example 2


### Run example 2
```
/home/test/.local/bin/jupyter-lab keras-elephone.py 
```
### Results

<img src="./example2/integrated_gradients_3_1.png" width="300">

<img src="./example2/integrated_gradients_9_1.png" width="900">

### Issues

* TODO

## References
* https://keras.io/examples/vision/integrated_gradients/
* https://arxiv.org/pdf/1703.01365.pdf


