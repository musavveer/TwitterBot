import tweepy
import time
import os
from os import environ


API_key = environ['API_key']
API_key_secret = environ['API_key_secret'] 
Access_token = environ['Access_token']
Access_token_secret = environ['Access_token_secret']



auth = tweepy.OAuthHandler( API_key, API_key_secret)
auth.set_access_token(Access_token, Access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


user = api.me()

search = '#100DaysOfCode'
numTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(numTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        print("Retweet done")
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break    
