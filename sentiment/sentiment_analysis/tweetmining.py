import tweepy
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getHomePageTweets():
    pass

def getUserTweets():
    pass

def getHashTagTweets():
    pass