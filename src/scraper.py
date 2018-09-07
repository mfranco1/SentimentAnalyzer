import os
import json
import codecs
import tweepy
from tweepy import OAuthHandler
import facepy
from facepy import GraphAPI
import praw

def tweet_print(api):
    f = codecs.open('res/raw_twitter_data.txt', 'a', encoding='utf8')
    for tweet in tweepy.Cursor(api.search, q="factset").items(1000):
        json_tweet = tweet._json
        text, date, location, url = (str(json_tweet['text']), str(json_tweet['created_at']), str(json_tweet['geo']), str(json_tweet['source']))
        f.write("|".join([text, date, location, url]) + "\n")
    f.close()

def tweet_connect():
    consumer_key = os.getenv('consumer_key','')
    consumer_secret = os.getenv('consumer_secret','')
    access_token_key = os.getenv('access_token_key','')
    access_token_secret = os.getenv('access_token_secret','')

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)
    tweet_print(api)

def reddit_print(api):
    results = api.search('factset', subreddit=None, sort=None, syntax=None, period=None)

def reddit_connect():
    api = praw.Reddit(user_agent='Connecting to Reddit')
    username = os.getenv('reddit_username','')
    password = os.getenv('reddit_password','')
    api.login(username, password, disable_warning=True)
    reddit_print(api)

def fb_print():
    pass

def fb_connect():
    fb_print()

def main():
    tweet_connect()
    reddit_connect()
    fb_connect()

if __name__ == "__main__":
    main()




"""import scrapy

class FdsSpider(scrapy.Spider):
    name = "fds_spider"
    start_urls = ['https://reddit.com']
"""
