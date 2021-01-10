import tweepy
from time import sleep
from credentials import *


auth = tweepy.OAuthHandler( API_key, API_key_secret)
auth.set_access_token(Access_token, Access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


user = api.me()

search = '#100DaysOfCode'

for tweet in tweepy.Cursor(api.search, search).items():
    try:
        
        tweet.favorite()
        print('Tweet Liked')
        

        tweet.retweet()
        print("Retweet done")

        sleep(100)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break    
