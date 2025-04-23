import tensorflow as tf
from keras import *

class PlayerPerformancePredictor(tf.keras.Model):
    def __init__(self, num_features):
        super().__init__()
        self.dense1 = tf.keras.layers.Dense(64, activation = 'relu')
        self.dropout = tf.keras.layers.Dropout(0.2)
        self.output_layer = tf.keras.layers.Dense(1)

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dropout(x)
        return self.output_layer(x)
