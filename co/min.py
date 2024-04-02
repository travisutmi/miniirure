import requests

# Make a GET request to a website
response = requests.get("https://www.example.com Check the status code of the response
if response.status_code == 200:
    # Print the content of the response
    print(response.content)
else:
    # Print an error message
    print("Something went wrong!")
