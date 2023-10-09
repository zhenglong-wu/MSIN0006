import tweepy as tw
from dotenv import load_dotenv
load_dotenv()
import os


auth = tw.OAuthHandler(consumer_key=os.getenv('twitter_api_key'),
                       consumer_secret=os.getenv('twitter_api_key_secret'))
auth.set_access_token(key=os.getenv('twitter_access_token'), 
                      secret=os.getenv('twitter_access_token_secret'))

api = tw.API(auth=auth, 
             wait_on_rate_limit=True)


tweets = tw.Cursor(api.search_tweets, 
                   q='#harrypotter',
                   lang ='en',
                   since='2021-05-28').items(50)

tweet_details = [[tweet.text,
                  tweet.user.screen_name,
                  tweet.user.location]for tweet in tweets]

print(tweet_details)