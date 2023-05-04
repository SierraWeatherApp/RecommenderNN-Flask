# jacket_model.py

from app.utils import input_data, jacket_data, create_and_train_model
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
x_train, x_test, y_train_jacket, y_test_jacket = train_test_split(input_data, jacket_data, test_size=0.2)

# Convert the data to float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Create and train the jacket model with a custom optimizer and learning rate
jacket_model = create_and_train_model(x_train,y_train_jacket,(11,),jacket_data.shape[1], 'rmsprop', 0.001)

jacket_model.save('trained/jacket-m.h5')
