import numpy as np
import os
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

def getPrediction(filename):

    # Loading the model
    new_model = load_model(os.path.join('models', 'fgg_happy_sad_model.h5'))

    # Loading the image
    img_path = 'static/uploaded_images/' + filename

    img = cv2.imread(img_path)

    # Resize uploaded images to same size as training images.
    resize = tf.image.resize(img, (256, 256))

    predict = new_model.predict(np.expand_dims(resize/255, 0))

    if predict > 0.5:
        label = 'Sad'
        return label +' with a probability of ' + str(round(predict[0][0]*100, 2)) + '%'
    else:
        label = 'Happy'
        return label +' with a probability of ' + str(round(100-(predict[0][0]*100), 2)) + '%'


      

