#!/usr/bin/env python3
import praw
import tweepy
import json

reddit = praw.Reddit('rPyBot')
subreddit = reddit.subreddit("dadjokes")
with open("data.txt", "w") as filename:
    for submission in subreddit.hot(limit=1):
        filename.write(submission.title+'\n')
        filename.write(submission.selftext)

with open('bot_config.json', 'r') as f:
    config = json.load(f)

CONSUMER_KEY = config['TWITTER']['CONSUMER_KEY']
CONSUMER_SECRET = config['TWITTER']['CONSUMER_SECRET']
ACCESS_KEY = config['TWITTER']['ACCESS_KEY']
ACCESS_SECRET = config['TWITTER']['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open("data.txt", "r") as filename:
    sub_data = filename.readlines()
    # print(sub_data)
    to_print = ""
    for line in sub_data:
        to_print = to_print + line
    # print(to_print)
    api.update_status(to_print)

print("Dad joke for the day tweeted !")
