#!/usr/bin/env python2.7  
# twitterwin.py by Alex Eames https://raspi.tv/?p=5281  
import tweepy  
import random  
  
# Consumer keys and access tokens, used for OAuth  
consumer_key = '6gTma2ITYHEh7MZMRJaflnxK7'  
consumer_secret = 'a20hHEbN1qudaR6RAdMCHtPKdOjpjiiNKabXjhj52Ajb4uHz2S'  
access_token = '1051987549487534081-quzVSEUw33JJiImQ7mSnyvZvdTsmln'  
access_token_secret = 'Uz5w4bC3heTN3efnA5yuh7lOZZMzYzkZYThykqRgnZUtu' 
  
# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
  
# Creation of the actual interface, using authentication  
api = tweepy.API(auth)  
  
follow2 = api.followers_ids() # gives a list of followers ids  
print "you have %d followers" % len(follow2)  
  
show_list = raw_input("Do you want to list the followers array?")  
if show_list in ('y', 'yes', 'Y', 'Yes', 'YES'):  
    print follow2  
  
def pick_winner():  
    random_number = random.randint(0, len(follow2)-1)  
    winner = api.get_user(follow2[random_number])  
    print winner.screen_name, random_number  
  
while True:  
    pick = raw_input("Press Enter to pick a winner, Q to quit.")  
    if pick in ('q', 'Q','quit', 'QUIT', 'Quit'):  
        break  
    pick_winner()  