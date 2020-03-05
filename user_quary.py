#!/usr/bin/env python3.7
import tweepy
from tweepy import OAuthHandler
import time as timeto
import json
import pandas as pd

with open('twit_cred.json') as cred_data:
	info = json.load(cred_data)
	consumer_key = info['CONSUMER_KEY']
	consumer_secret = info['CONSUMER_SECRET']
	access_token = info['ACCESS_KEY']
	access_token_secret = info['ACCESS_SECRET']

authentication = OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = input('Enter twitter handler: ')
count = 200

tweets = []

def username_tweets_to_csv(username,count):
    try: 
        for tweet in api.user_timeline(id=username, count=count):
            tweets.append((tweet.created_at,tweet.id,tweet.text))
            tweetsdf = pd.DataFrame(tweets,columns=['Datetime', 'Tweet Id', 'Text'])
            tweetsdf.to_csv('./media/{}-tweets1.csv'.format(username)) 

    except BaseException as e:
          print('failed on_status,',str(e))
          timeto.sleep(3)

all_tweets = api.user_timeline(screen_name=user, count=200, include_rts=False, exclude_replies=True)
last_tweet_id = all_tweets[-1].id


username_tweets_to_csv(user, count)
