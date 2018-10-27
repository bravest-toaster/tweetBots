#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bot Tutorial Step 2 / bot number 2

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/@CSCC_Linux_Bot

# This bot tweets a random line from a text file
# given period of time between tweets.


import tweepy, time
from credentials import *
from random import randint

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet
filename = open('userchoice.txt','r') 
tweet_text = filename.readlines() 
filename.close()

# a function that picks a random line
def line_number():
    return randint(0, len(tweet_text) - 1)


line = tweet_text[line_number()]
api.update_status(status=line)
print(line)
time.sleep(15) # Sleep for 15 seconds


# To quit early: CTRL+C and wait a few seconds
