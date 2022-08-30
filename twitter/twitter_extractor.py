import pandas as pd

class TweetExtractor(object):

    """
        Function will parse and create a dataframe
    """

    def __init__(self, tweet_list):
        self.tweet_list = tweet_list

    def get_created_time(self)->list:
        time = [tweet['created_at'] for tweet in self.tweet_list]
        return time
    
    def get_id(self)->list:
        id = [id['id'] for id in self.tweet_list]
        return id
    
    def get_screen_name(self)->list:
        name = [name['user']['screen_name'] for name in self.tweet_list]
        return name
    
    def get_source(self)->list:
        source = [source['source'] for source in self.tweet_list]
        return source
    
    def get_user_mentions(self)->list:
        total = []
        for tweet in self.tweet_list:
            total.append([(user_mentions['id'], user_mentions['name']) for user_mentions in tweet['entities']["user_mentions"]])
        return total

    def get_full_text(self)->list:
        text = [text['full_text'] for text in self.tweet_list]
        return text

    

    def get_tweets_df(self)->pd.DataFrame:

        # Columns to be generated
        columns = ['created_at', 'id', 'screen_name','full_text' ,'source' , 'user_mentions']

        created_at = self.get_created_time()
        id_num = self.get_id()
        screen_name = self.get_screen_name()
        text = self.get_full_text()
        source = self.get_source()
        user_mentions = self.get_user_mentions()

        tweets_data = zip(created_at, id_num, screen_name, text, source, user_mentions)

        df = pd.DataFrame(data=tweets_data, columns=columns)

        return df
