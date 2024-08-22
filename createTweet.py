import tweepy
import logging
from dotenv import load_dotenv
import os

load_dotenv()


# api_key = os.getenv('API_KEY')
# api_key_secret = os.getenv('API_KEY_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

response = client.create_tweet(
    text="First tweet using Tweepy - 1"
)

# print(f"https://twitter.com/user/status/{response.data['id']}")





