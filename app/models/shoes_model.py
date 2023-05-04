# shoes_model.py

from app.utils import input_data, shoes_data, create_and_train_model
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
x_train, x_test, y_train_shoes, y_test_shoes = train_test_split(input_data, shoes_data, test_size=0.2)

# Convert the data to float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Create and train the shoes model with a custom optimizer and learning rate
shoes_model = create_and_train_model(x_train,y_train_shoes,(11,),shoes_data.shape[1], 'adam', 0.001)

#shoes_model.save('trained/shoes-m.h5')
