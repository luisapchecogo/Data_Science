import json_to_list as jl
from twitter_extractor_class import TweetExtractor
from sentiment_analysis_spanish import sentiment_analysis
import numpy as np



tweet_list = jl.read_json('twitter_test.json')

tweet = TweetExtractor(tweet_list)
tweet_df = tweet.get_tweets_df()

sentiment = sentiment_analysis.SentimentAnalysisSpanish()

temp = []
for tweet in tweet_df['full_text']:
    temp.append(sentiment.sentiment(tweet))

tweet_df['ponder'] = [np.nan for _ in range(tweet_df.shape[0])]

for i in range(tweet_df.shape[0]):
    tweet_df['ponder'][i] = temp[i]

tweet_df['sentiment'] = [np.nan for _ in range(tweet_df.shape[0])]

countP = 0
countN = 0
for i in range(tweet_df.shape[0]):
    if tweet_df['ponder'][i] > 0.5:
        tweet_df['sentiment'][i] = 'positive'
        countP+=1
    elif tweet_df['ponder'][i] == 0.5:
        tweet_df['sentiment'] = 'neutral'
    else:
        tweet_df['sentiment'][i] = 'negative'
        countN+=1
 

print(f'porcentaje de tweets negativos es : {(countN/(countN+countP))*100}')
print(f'porcentaje de tweets positivos es : {(countP/(countN+countP))*100}')
