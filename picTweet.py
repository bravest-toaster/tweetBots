
import tweepy  
from subprocess import call  
from datetime import datetime  
   
i = datetime.now()               #take time and date for filename  
now = i.strftime('%Y%m%d-%H%M%S')  
photo_name = now + '.jpg'  
cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name   
call ([cmd], shell=True)         #shoot the photo  
  
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
  
# Send the tweet with photo  
photo_path = '/home/pi/' + photo_name  
status = 'Photo auto-tweet from Pi: ' + i.strftime('%Y/%m/%d %H:%M:%S')   
api.update_with_media(photo_path, status=status) 