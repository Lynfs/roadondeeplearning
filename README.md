**This file was NOT completely written by me. there are copies of explanations from other sources, such as towards and imasters.**

# Basics informations about neural networks

### What exactly is Deep Learning?

Deep Learning is a subset of Machine Learning, which on the other hand is a subset of Artificial Intelligence. Artificial Intelligence is a general term that refers to techniques that enable computers to mimic human behavior. Machine Learning represents a set of algorithms trained on data that make all of this possible.

![](https://miro.medium.com/max/530/0*DTXj4uIfDmtDyL0z)

Deep Learning, on the other hand, is just a type of Machine Learning, inspired by the structure of a human brain. Deep learning algorithms attempt to draw similar conclusions as humans would by continually analyzing data with a given logical structure. To achieve this, deep learning uses a multi-layered structure of algorithms called neural networks.

![](https://miro.medium.com/max/700/0*AONVmd3v4wO_dWr6)

so, we can call Deep learning as a "Deep neural-network", cuz the adjective "deep" in comes from the use of multiple layers in the network. Lets see a quicly example of how it works with images.

![](https://static.imasters.com.br/wp-content/uploads/2018/06/19154808/grey1.jpg)

### Convolutional Neural Network

Convolution can be seen as a synonym for combination. It is the procedure of combining two sources of information.

Convolutional Neural Network (CNN) is a class of neural network used for image processing and analysis. It was proposed in 1998 in a paper by scientist Yann LeCun, who proposed an architecture capable of recognizing handwritten digits with 99.2% precision. This architecture was inspired by a 1968 research by David Hunter Hubel and Torsten Wiesel on the functioning of the visual cortex of mammals.

Research suggests that mammals visually perceive the world hierarchically, through layers of neuron clusters. When we see something, clusters are activated hierarchically, and each detects a set of attributes about what was seen.

CNN's architecture simulates neuron clusters to detect attributes of what has been seen, organized hierarchically and abstractly enough to generalize regardless of size, rotation position, etc.

![](https://static.imasters.com.br/wp-content/uploads/2018/06/19154902/2.png)

An image can be represented as a matrix. Each element of the matrix contains the value of its respective pixel, which can vary from 0 to 255. For color images in RGB, we have a matrix “in three dimensions”, where each dimension is one of the layers of color (red, green and blue ). Thus, a color image of 255px by 255px is represented by three arrays of 255 by 255 (255x255x3).

so, what could we do to "learn patterns"?

we can use a smaller matrix, composed of values. It will be applied to the image (as a filter), to obtain activation regions, that is, regions where specific attributes of this filter were found.

For example, we can imagine a 16 x 16 filter traversing a 256 x 256 x 3 image. At each step we take a 16 x 16 portion of the image and make a convolution (that is, we calculate the scalar product between the two matrices) . The obtained value is added to the activation matrix. This process is repeated until all three matrices have been completely traversed.

![](https://static.imasters.com.br/wp-content/uploads/2018/06/19154939/3-300x219.gif)

The filter values change with each training iteration in order to improve the identification of which regions contain significant attributes (in the same way that the weights in a neural network perceptron are updated in training).

But how does this series of multiplications help us to detect the attributes of an image? As the filter learns to detect an attribute (through the learning process), its values adjust so that the result of the convolution is a value that indicates that the given attribute has been found.

In the example below, we are trying to identify the mouse in the image. The filter will work to detect that curve highlighted in yellow. The pixel representation of the mouse outline contains color values where the outline occurs, and zero (white) where it does not.

![](https://static.imasters.com.br/wp-content/uploads/2018/06/19155014/lines1.jpg)

When we scale the product between the filter and the contour we are looking for, the result is a very large number.

![](https://static.imasters.com.br/wp-content/uploads/2018/06/19155051/graeen.jpg)

*This result is always lower in other parts of the image, because the scalar product is smaller.*

![](https://static.imasters.com.br/wp-content/uploads/2018/06/19155116/MOUSE.jpg)

So, when the result of the convolution is a large number, it means that the attribute was detected. When it is a result of 0 or very small, it means that the attribute was not found.

[Original source](https://imasters.com.br/back-end/classificacao-de-imagens-com-deep-learning-e-tensorflow)

## below, some simple definitions involved in the middle

### What's a activation function? 

well, it’s just a thing function that you use to get the output of node. It is also known as Transfer Function.

### Why we use Activation functions with Neural Networks?

It is used to determine the output of neural network like yes or no. It maps the resulting values in between 0 to 1 or -1 to 1 etc. (depending upon the function).

## Sigmoid function

**it is given by :** ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/faaa0c014ae28ac67db5c49b3f3e8b08415a3f2b)


![sigmoid](https://i.imgur.com/c9R8y1L.png)

## Tanh 

 **it is given by**:  ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4f1b5f1173b93d23c64a0d3508028f8649a5a14e)

![enter image description here](https://i.imgur.com/XwT3bSo.png)

## What's derivative?

(wikitime): The derivative of a function of a real variable measures the sensitivity to change of the function value (output value) with respect to a change in its argument (input value). Derivatives are a fundamental tool of calculus. For example, the derivative of the position of a moving object with respect to time is the object's velocity: this measures how quickly the position of the object changes when time advances.

The derivative of a function of a single variable at a chosen input value, when it exists, is the slope of the tangent line to the graph of the function at that point. The tangent line is the best linear approximation of the function near that input value. For this reason, the derivative is often described as the "instantaneous rate of change", the ratio of the instantaneous change in the dependent variable to that of the independent variable.

![enter image description here](https://i.imgur.com/fJgBHak.png)

## why do we need to use the derivative?

When updating the curve, to know in which direction and how much to change or update the curve depending upon the slope.That is why we use differentiation in almost every part of Machine Learning and Deep Learning.

![enter image description here](https://i.imgur.com/WkrVhWk.png)

## What's a loss function?

It’s a method of evaluating how well specific algorithm models the given data. If predictions deviates too much from actual results, loss function would cough up a very large number. Gradually, with the help of some optimization function, loss function learns to reduce the error in prediction. In this article we will go through several loss functions and their applications in the domain of machine/deep learning.

**L2 loss:**

![](https://miro.medium.com/max/1026/1*SGhoeJ_BgcfqU06CmX41rw.png)

**L1 loss:**

![](https://miro.medium.com/max/1066/1*piCo0iDgPmESnQkHSwAK6A.png)

**Mean Bias Error:**

![](https://miro.medium.com/max/992/1*BpYT_vpYizQpeY3bGuvTbw.png)

## What's a cost function?

It is a function that  **measures the performance of a Machine Learning model**  for given data. Cost Function quantifies the error between predicted values and expected values and  **presents it in the form of a single real number**. Depending on the problem Cost Function can be formed in many different ways. The purpose of Cost Function is to be either:

-   **Minimized** - then returned value is usually called  **cost**,  **loss**  or  **error**. The goal is to find the values of model parameters for which Cost Function return as small number as possible.
-   **Maximized** - then the value it yields is named a  **reward**. The goal is to find values of model parameters for which returned number is as large as possible.

**Mean Absolute Error** it's given by:
![mae example](https://miro.medium.com/max/261/0*Swic0H6aelUyYI2B.png)

## What's gradient descent?

Gradient descent is an optimization algorithm used to minimize some function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient. In machine learning, we use gradient descent to update the parameters of our model.
