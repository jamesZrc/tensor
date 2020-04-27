import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt


model = tf.keras.models.load_model('D:/tensor/model/mnist')

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

predictions = model.predict(np.array([x_test[5]]))
print(np.argmax(predictions))