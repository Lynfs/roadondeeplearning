# Basics informations about neural networks

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
