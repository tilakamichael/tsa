import tweepy
import config
import tweepy

def getClient():
    client = tweepy.Client(bearer_token=config.bearer_token, 
                           consumer_key=config.consumer_key,
                           consumer_secret=config.consumer_key_secret,
                           access_token=config.access_token,
                           access_token_secret=config.access_token_secret)
    
    return client

def scrapeQuery(query, count):
    client = getClient()
    
    tweets = client.search_recent_tweets(query=query, max_results=count)
    tweetData = tweets.data
    textList = []
    
    if not tweetData is None and len(tweetData) > 0:
        for tweet in tweetData:
            textList.append(tweet.text)
            
    return textList