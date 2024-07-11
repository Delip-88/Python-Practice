import requests

# URL of the API
url = "https://jsonplaceholder.typicode.com/users"

# Send a GET request to the URL
response = requests.get(url)

# Parse the response text as JSON
users_data = response.json()

# Initialize a list to store user information
users = []

# Iterate through each item in the users_data
for user_data in users_data:
    # Create a dictionary with the name and email
    user_info = {'name': user_data['username'], 'email': user_data['email']}
    # Append the dictionary to the users list
    users.append(user_info)

# Print each user info dictionary and its type
# for user_info in users:
#     print(user_info, type(user_info))

# # Print the type of the users list
# print(type(users))


for u in users:
    if u['name'].lower() == 'bret':
        print(u['name'], u['email'])