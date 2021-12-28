# Handles the authentication of the Reddit API

import requests

clientID = 'your_client_ID'
secretKey = 'your_secret_key'

auth = requests.auth.HTTPBasicAuth(clientID, secretKey)

# OPTIONAL: store the password in a separate file, read the file and store in a variable.
# Use the variable in the data dictionary to gain access to reddit.com
f = open('pw.txt', 'r')
pw = f.read()

# tell Reddit we're using a password to login then provide the password
data = {
    'grant_type': 'password',
    'username': 'ben-meyer',
    'password': pw
}

# Create headers for Reddit to tell it what we're doing.
headers = {'User-Agent': 'MemeOfTheDay'}

# Go to Reddit API and provide the clientID & key, username, password and the headers
response = requests.post('https://www.reddit.com/api/v1/access_token',
                         auth=auth, data=data, headers=headers)

# Reddit will then give you an access token which we can store in a variable.
TOKEN = response.json()['access_token']

# Add the Authorization token into the headers variable.
headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}

# TEST AUTH CONNECTION
# me = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()
# print(me)