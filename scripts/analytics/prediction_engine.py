from tensorflow.keras.layers import LSTM, Dense

def build_performance_model(input_shape):
    model = tf.keras.Sequential([
        LSTM(64, input_shape = input_shape, return_sequences = True),
        LSTM(32),
        Dense(16, activation ='relu'),
        Dense(1, activation ='linear')
    ])
    model.compile(loss = 'mse', optimizer = 'adam')
    return model