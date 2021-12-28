# Handles sending the reddit message to the Slack API

import requests
from reddit_functions import slackMessage


def send_slack_message(message):
    message = message + '?utm_medium=android_app&utm_source=share'
    payload = '{"text": "%s"}' % message
    response = requests.post('YOUR_SLACK_WEBHOOK',
                             data=payload)
    print(response.text)


send_slack_message(slackMessage)
