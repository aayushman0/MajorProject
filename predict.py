import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('model.h5')

def predict(frame):
    frame = cv2.resize(frame, (50, 50))
    frame = np.array(frame)
    frame = frame.reshape((1, 50, 50, 1))
    frame = frame.astype('float32') / 255
    prediction = model.predict(frame)
    
    vals = ''
    for n in prediction:
        n = np.round(n * 100)
        vals = vals + str(n) + ' '
    
    return vals, prediction
    