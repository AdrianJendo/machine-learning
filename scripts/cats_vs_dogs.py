import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random
import os

# define image properties
IMG_WIDTH=128
IMG_HEIGHT=128
IMG_SIZE=(IMG_WIDTH,IMG_HEIGHT)
IMG_CHANNELS=3

# prepare dataset for training model
filenames=os.listdir("./training_data/cats_vs_dogs")

categories=[]
for f_name in filenames:
    category=f_name.split('.')[0]
    if category=='dog':
        categories.append(1)
    else:
        categories.append(0)

df=pd.DataFrame({
    'filename':filenames,
    'category':categories
})

