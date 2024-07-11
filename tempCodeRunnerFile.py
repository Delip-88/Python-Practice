import requests

# URL of the API
url = "https://jsonplaceholder.typicode.com/users"

# Send a GET request to the URL
response = requests.get(url)

# Parse the response text as JSON
news = response.json()

# Initialize list to store username
username = []

# Iterate through each item in the news
for n in news:
    # Append the title to the username list
    username.append(n['username'])

# Print the list of username
for i in username:
    print(i)
