import json
import config
import tweepy
import time


# Define the config variables
api_key = config.twitter_api['consumer_key']
api_secret = config.twitter_api['consumer_secret']
access_token = config.twitter_api['access_token']
access_token_secret = config.twitter_api['access_token_secret']

# authenticate twitter developer api
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# list of specific keywords
keywords = '#PetroPresidente OR @petrogustavo OR @infopresidencia OR #Colombia'
limit = 900

# Save twitter content in a json file
c = tweepy.Cursor(
    api.search_tweets,
    q=keywords,
    tweet_mode='extended',
    include_entities=True, 
).items(limit=limit)

while True:
    try:
        tweet = c.next()
        with open('twitter_test.json', 'a', encoding='utf-8') as f:
            data = tweet._json
            f.write(json.dumps(data))
            f.write('\n')
    except:
        print('Limit reached.')
        time.sleep(15*60)
        continue
