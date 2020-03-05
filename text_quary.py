#!/usr/bin/env python3.7
import tweepy
from tweepy import OAuthHandler
import time as timeto
import pandas as pd
import json

with open('./creds/twit_cred.json') as cred_data:
	info = json.load(cred_data)
	consumer_key = info['CONSUMER_KEY']
	consumer_secret = info['CONSUMER_SECRET']
	access_token = info['ACCESS_KEY']
	access_token_secret = info['ACCESS_SECRET']

authentication = OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

text_query = input('Enter twitter handler: ')
count = 200

tweets = []

def text_query_to_csv(text_query,count):
    try:
        for tweet in api.search(q=text_query, count=count):
          tweets.append((tweet.created_at,tweet.id,tweet.text))
          tweetsdf = pd.DataFrame(tweets,columns=['Datetime', 'Tweet Id', 'Text'])
          tweetsdf.to_csv('./media/{}-tweets2.csv'.format(text_query)) 
    except BaseException as e:
        print('failed on_status,',str(e))
        timeto.sleep(3)

text_query_to_csv(text_query, count)