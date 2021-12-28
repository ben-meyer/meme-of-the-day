# Handles the reddit related functions of the bot

import requests
from reddit_auth import headers

# Use /hot /top /new or other endpoints in this API call
hotProgrammerHumour = requests.get('https://oauth.reddit.com/r/ProgrammerHumor/hot', headers=headers).json()

# Create a blank list to store urls of the posts
post_urls = []

# Iterate through the json object to extract the URLs of all the posts found in the API call.
# Store the urls in the list created above. The API returns about 20 - 30 URLs.
for post in hotProgrammerHumour['data']['children']:
    post_urls.append('https://www.reddit.com' + str(post['data']['permalink']))

# Store the first true URL as the Slack message. As it is first, it is therefore, the 'hottest'.
slackMessage = post_urls[0]