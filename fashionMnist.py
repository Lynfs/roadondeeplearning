import tensorflow as tf
from tensorflow import keras
import numpy as np

#dataset import
fashioMnist = keras.datasets.fashioMnist
#separate
(trainImages, trainLabels), (testImages, testLabels) = fashioMnist.load_data()
classes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
#normalize
trainImages = trainImages / 255.0
testImages = testImages / 255.0
#set the model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
#compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(trainImages, trainLabels, epochs=10)
testLoss, test_acc = model.evaluate(testImages,  testLabels, verbose=0)
print('\nAccuracy Test:', test_acc)
predictions = model.predict(testImages)

img = testImages[0]
img = (np.expand_dims(img,0))
predict = model.predict(img)
print('\nprediction: ', predict)
