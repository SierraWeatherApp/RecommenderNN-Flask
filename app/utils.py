# utils.py

import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv('~/KTH/GitHub/RecommenderNN-Flask/app/encoded_data.csv')

# Split the data into input and output
input_data = data.iloc[:, :11]
output_data = data.iloc[:, 11:]

# Split the output data into separate categories
head_data = output_data[['head_beanie', 'head_cap', 'head_empty']]
shirt_data = output_data[['shirt_hoodie', 'shirt_long-sleeve', 'shirt_t-shirt']]
jacket_data = output_data[['jacket_empty', 'jacket_light', 'jacket_winter']]
pants_data = output_data[['pants_pants', 'pants_shorts', 'pants_snow-pants']]
shoes_data = output_data[['shoes_boots', 'shoes_rain-boots', 'shoes_sandals', 'shoes_sneakers']]
umbrella_data = output_data[['umbrella_False', 'umbrella_True']]


# Define a function to create and train a model for a given category
def create_and_train_model(x_train, y_train, input_shape, num_classes, optimizer_in, learning_rate):
    # Create the model
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(64, activation='relu', input_shape=input_shape))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))

    # Create the optimizer
    optimizer = tf.keras.optimizers.get(optimizer_in)
    # tf.keras.backend.set_value(optimizer.lr, learning_rate) #comment back in to change learning rate

    # Compile the model
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=10)
    return model
