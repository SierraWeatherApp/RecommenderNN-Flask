import requests

# Define the base URL of your Flask API
base_url = 'http://localhost:5000'
# Define the input values as a list
inputs = [12.5, 16.1, 52, 17.9, 50, 0.0, 1, 1, 1, 5, 3]
# Send a GET request to the /rec route with the input values as query parameters
response = requests.get(f'{base_url}/rec', params={'inputs': inputs})

# Check the response status code
if response.status_code == 200:
    # The request was successful
    # Get the response data
    data = response.json()
    # Use the response data
else:
    # The request failed
    # Handle the error
    data = "request failed"
print(data)
