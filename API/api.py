import requests

# Define the API endpoint URL
api_url = "https://jsonplaceholder.typicode.com/posts/1" # Example public API

try:
    # Send a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        data = response.json()
        print("API call successful!")
        print("Data received:")
        print(data)
    else:
        print(f"API call failed with status code: {response.status_code}")
        print(f"Error message: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")