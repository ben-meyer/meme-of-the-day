# meme-of-the-day

Grabs the hottest post from r/ProgrammerHumor and posts it to a Slack channel via an incoming webhook.

| File | Purpose |
|---|---|
| `reddit_functions.py` | Fetches the hot post and builds the message |
| `reddit_auth.py` | Reddit credentials |
| `main.py` | Posts the message to Slack |

## Setup

```bash
pip install requests praw
```

1. Put your Reddit credentials in `reddit_auth.py`
2. Put your Slack webhook URL in `main.py`
3. Run `python main.py` — e.g. from cron for a daily meme.
