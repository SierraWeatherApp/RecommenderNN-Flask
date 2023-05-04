# head_model.py

from app.utils import input_data, head_data, create_and_train_model
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
x_train, x_test, y_train_head, y_test_head = train_test_split(input_data, head_data, test_size=0.2)

# Convert the data to float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Create and train the head model with a custom optimizer and learning rate
head_model = create_and_train_model(x_train, y_train_head,(11,), head_data.shape[1], 'sgd', 0.01)

head_model.save('trained/head-m.h5')
