import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
import json
consumer_key = "6gTma2ITYHEh7MZMRJaflnxK7"
consumer_secret = "a20hHEbN1qudaR6RAdMCHtPKdOjpjiiNKabXjhj52Ajb4uHz2S"
access_token = "1051987549487534081-quzVSEUw33JJiImQ7mSnyvZvdTsmln"
access_secret = "Uz5w4bC3heTN3efnA5yuh7lOZZMzYzkZYThykqRgnZUtu"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('FILENAME.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
#Set the hashtag to be searched
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#Linux'])
