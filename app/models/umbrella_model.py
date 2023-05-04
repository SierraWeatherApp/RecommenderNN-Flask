# umbrella_model.py

from app.utils import input_data, umbrella_data, create_and_train_model
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
x_train, x_test, y_train_umbrella, y_test_umbrella = train_test_split(input_data, umbrella_data, test_size=0.2)

# Convert the data to float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Create and train the umbrella model with a custom optimizer and learning rate
umbrella_model = create_and_train_model(x_train,y_train_umbrella,(11,),umbrella_data.shape[1], 'sgd', learning_rate=0.01)

umbrella_model.save('trained/umbrella-m.h5')
