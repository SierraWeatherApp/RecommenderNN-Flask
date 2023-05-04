from sklearn.model_selection import train_test_split

from models.head_model import head_model
from models.shirt_model import shirt_model
from models.jacket_model import jacket_model
from models.pants_model import pants_model
from models.shoes_model import shoes_model
from models.umbrella_model import umbrella_model
from utils import input_data, head_data, shirt_data, jacket_data, pants_data, shoes_data, umbrella_data


# Define a function to create and train a model for a given category
# Split the data into training and testing sets
x_train, x_test, y_train_head, y_test_head = train_test_split(input_data, head_data, test_size=0.2)
_, _, y_train_shirt, y_test_shirt = train_test_split(input_data, shirt_data, test_size=0.2)
_, _, y_train_jacket, y_test_jacket = train_test_split(input_data, jacket_data, test_size=0.2)
_, _, y_train_pants, y_test_pants = train_test_split(input_data, pants_data, test_size=0.2)
_, _, y_train_shoes, y_test_shoes = train_test_split(input_data, shoes_data, test_size=0.2)
_, _, y_train_umbrella, y_test_umbrella = train_test_split(input_data, umbrella_data, test_size=0.2)

# Convert the data to float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')


def display_results(model, x, y, category):
    # Generate predictions for the test data
    y_pred = model.predict(x)

    # Convert the predictions and actual results to class labels
    y_pred_labels = y_pred.argmax(axis=1)
    y_test_labels = y.values.argmax(axis=1)

    # Display the predicted and actual results
    print(f'{category}:')
    for i in range(5):
        print(f'Predicted: {y_pred_labels[i]}, Actual: {y_test_labels[i]}')
    print()


# Display the predicted and actual results for each category
display_results(head_model, x_test, y_test_head, 'Head')
display_results(shirt_model, x_test, y_test_shirt, 'Shirt')
display_results(jacket_model, x_test, y_test_jacket, 'Jacket')
display_results(pants_model, x_test, y_test_pants, 'Pants')
display_results(shoes_model, x_test, y_test_shoes, 'Shoes')
display_results(umbrella_model, x_test, y_test_umbrella, 'Umbrella')
