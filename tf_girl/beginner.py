# -*- encoding: utf-8 -*-
# @File:   beginner.py    
# @Time: 2020-05-29 14:37
# @Author: ZHANG
# @Description: beginner


import tensorflow as tf
from loguru import logger

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
logger.info(predictions)

probabilities = tf.nn.softmax(predictions).numpy()
logger.info(probabilities)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

logger.info(loss_fn(y_train[:1], predictions).numpy())

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test, y_test, verbose=2)

# wrap the trained model, attach the softmax to it. In order to return a probability.
probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])

logger.info(probability_model(x_test[:5]))

