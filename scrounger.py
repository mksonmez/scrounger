#!/usr/bin/env python
# encoding: utf-8


import tweepy, time, json
import pandas as pd

with open('twit_cred.json') as cred_data:
	info = json.load(cred_data)
	consumer_key = info['CONSUMER_KEY']
	consumer_secret = info['CONSUMER_SECRET']
	access_token = info['ACCESS_KEY']
	access_token_secret = info['ACCESS_SECRET']

cred_data = tweepy.OAuthHandler(consumer_key, consumer_secret)
cred_data.set_access_token(access_token, access_token_secret)
api = tweepy.API(cred_data,wait_on_rate_limit=True)

tweets = []

def username_tweets_to_csv(username,count):
    try: 
        for tweet in api.user_timeline(id=username, count=count):
            tweets.append((tweet.created_at,tweet.id,tweet.text))
            tweetsdf = pd.DataFrame(tweets,columns=['Datetime', 'Tweet Id', 'Text'])
            tweetsdf.to_csv('{}-tweets.csv'.format(username)) 

    except BaseException as e:
          print('failed on_status,',str(e))
          time.sleep(3)

tweets = []

def text_query_to_csv(text_query,count):
    try:
        for tweet in api.search(q=text_query, count=count):
          tweets.append((tweet.created_at,tweet.id,tweet.text))
          tweetsdf = pd.DataFrame(tweets,columns=['Datetime', 'Tweet Id', 'Text'])
          tweetsdf.to_csv('{}-tweets.csv'.format(text_query)) 
    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)

# options
username = input('Enter twitter handler: ')
count = int(input('Enter a number to scrape: '))

text_query = input('Enter what to scrape: ')
count = int(input('Enter a number to scrape: '))

# outputs
username_tweets_to_csv(username, count)
text_query_to_csv(text_query, count)
