#!/usr/bin/env python2.7

import tweepy  
import sys  
import os  
from datetime import datetime  
from credentials import *
   
i = datetime.now()  
degree = unichr(176)         # code for degree symbol  

# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
   

  
if len(sys.argv) >= 2:        # use entered text as tweet  
    tweet_text = sys.argv[1]  
    print ' Tweeting: ' + tweet_text
  
else:                         # if no entered text, tweet the temp  
    now = i.strftime('%Y/%m/%d %H:%M:%S')  
    cmd = '/opt/vc/bin/vcgencmd measure_temp'  
    line = os.popen(cmd).readline().strip()  
    temp = line.split('=')[1].split("'")[0]  
    print now + ' Pi Processor Temperature is '+ temp + ' ' + degree +'C'  
    tweet_text = now + ' Pi Processor Temperature is '+ temp + ' ' + degree +'C'  
  
if len(tweet_text) <= 140: 
    api.update_status(status=tweet_text)  
else:  
    print "tweet not sent. Too long. 140 chars Max."  