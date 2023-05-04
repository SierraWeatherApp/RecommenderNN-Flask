import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load the data from the CSV file
data = pd.read_csv('output.csv')

# Select the columns to be one-hot encoded
cols_to_encode = data.columns[11:]

# Create a one-hot encoder object
encoder = OneHotEncoder(sparse=False)

# Fit the encoder on the data
encoder.fit(data[cols_to_encode])

# Transform the data using the encoder
encoded_cols = encoder.transform(data[cols_to_encode])

# Create a new dataframe with the encoded columns
encoded_data = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(cols_to_encode))

# Concatenate the original data and the encoded data
final_data = pd.concat([data, encoded_data], axis=1)

final_data.drop(['head', 'shirt', 'jacket', 'pants', 'shoes', 'umbrella'], axis=1, inplace=True)

# Save the final data to a new CSV file
final_data.to_csv('models/encoded_data.csv', index=False)
