# pants_model.py

from app.utils import input_data, pants_data, create_and_train_model
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
x_train, x_test, y_train_pants, y_test_pants = train_test_split(input_data, pants_data, test_size=0.2)

# Convert the data to float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Create and train the shoes model with a custom optimizer and learning rate
pants_model = create_and_train_model(x_train,y_train_pants,(11,),pants_data.shape[1], 'adam', 0.001)

#pants_model.save('trained/pants-m.h5')
