# shirt_model.py

from app.utils import input_data, shirt_data, create_and_train_model
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
x_train, x_test, y_train_shirt, y_test_shirt = train_test_split(input_data, shirt_data, test_size=0.2)

# Convert the data to float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Create and train the shirt model with a custom optimizer and learning rate
shirt_model = create_and_train_model(x_train,y_train_shirt,(11,),shirt_data.shape[1], 'sgd', 0.01)

shirt_model.save('trained/shirt-m.h5')
