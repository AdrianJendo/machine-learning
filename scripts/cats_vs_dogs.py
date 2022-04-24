import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random
import os

# define image properties
IMG_WIDTH = 128
IMG_HEIGHT = 128
IMG_SIZE = (IMG_WIDTH, IMG_HEIGHT)
IMG_CHANNELS = 3  # 3 channels (Red Green Blue)

# prepare dataset for training model
filenames = os.listdir("./training_data/cats_vs_dogs")

categories = []
for f_name in filenames:
    category = f_name.split(".")[0]
    if category == "dog":
        categories.append(1)
    else:
        categories.append(0)

df = pd.DataFrame({"filename": filenames, "category": categories})

# create neural net
from keras.models import Sequential
from keras.layers import (
    Conv2D,
    MaxPooling2D,
    Dropout,
    Flatten,
    Dense,
    Activation,
    BatchNormalization,
)

model = Sequential()
# apply convolution window to each section of the image
model.add(
    Conv2D(
        32,  # dimensionality of the output space (number of output filters)
        (3, 3),  # convolution window (3x3 matrix)
        activation="relu",
        input_shape=(IMG_WIDTH, IMG_HEIGHT, IMG_CHANNELS),  # needed for first layer
    )
)
model.add(BatchNormalization())  # normalize output from previous layer
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(128, (3, 3), activation="relu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(2, activation="softmax"))
model.compile(
    loss="categorical_crossentropy", optimizer="rmsprop", metrics=["accuracy"]
)

model.summary()
