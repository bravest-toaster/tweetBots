Team # 3 
Sam, Stephanie, and Mike
Project: 
Twitter Bot(s) on the Raspberry Pi











Introduction
Greetings, we are going to discuss creating your very own chat bot on Twitter with the help of Python and a Raspberry Pi. You can set up an entirely new account for this or you can set up some automation on a current Twitter account. We recommend using a new account for this as to not cause any potential problems with your existing Twitter. The purpose of this outline is to walk you through setting up access to Twitter’s API. We are proving an account for everyone to use if they choose to not create an account or run into problems setting it up. Due to the rampant abuse for harassment, misinformation campaigns, and alleged election meddling Twitter has really locked down API access. It used to be anyone could get one for any reason, now they’re a little pickier and you must ‘apply.’ 

 
So, while we encourage you to explore the possibilities that Twitter’s API + Python have to offer, it might not be feasible for everyone to sign up right before class. We ran some experiments and some accounts were approved, some weren’t. So, if you are following this tutorial outside our classroom, or you have your own account proceed below to Project Stage 1: API Access. If you want to use an account that we have setup ahead of time, please proceed to Project Stage 2: The Environment. The tutorial we will follow together will adhere to conditions that allow for everyone to hypothetically access the same account at the same time. How is this possible? The Twitter API is how

Project Stage 1: API Access
Step 0: Getting Started
Twitter is a web service that provides an application programing interface (API), which means you can write software that communicates with the live Twitter service—perhaps to read tweets in real time or to automatically publish tweets. API stands for Application Programming Interface. If you are not into development or software engineering the short explanation is it allows two applications to talk to each other. When you use an application on your mobile phone, the application connects to the Internet and sends data to a server. The server then retrieves that data, interprets it, performs the necessary actions and sends it back to your phone. The application then interprets that data and presents you with the information you wanted in a readable way. This is what an API is - all of this happens via API.  Twitter will not see multiple login attempts on this account because the interaction is via the API. The API is free to use, but you must have a Twitter account and to register your application to get access to the API, but that's easy enough. Twitter has very recently updated the process in which you obtain an API key.

Step 1: API Access
•	Start by visiting apps.twitter.com in your web browser
•	Click “Sign in” to log into your account
•	You will be brought to a window that looks like the picture below
 
With the example above my account needs to be verified. If you have not verified your account with an email address or phone number, you will need to do that to obtain API access. If you have verified your account properly you will see the same as above, with the exception that it will say “Continue” rather than “Add a valid phone number.” Follow whatever instructions (if given any) to properly verify your account. You will go back and forth between your email inbox, your mobile phone (if using a phone to verify) and this page.
you are already verified to meet Twitter’s expectations, then you will just need to click “continue.” After clicking “continue” or meeting the verification needs you will be taken to the screen shown below. Twitter needs to know if you are accessing as an organization, or an individual. 
 
•	You want to select “I am requesting access for my own personal use”
•	Then select a developer username
•	Select your country
•	Click “Continue”
Next you will be taken to the “Use Case” page. Here Twitter is asking to know a little more about you and your app / why you need API access. For this project I selected “Academic Research” and “Chatbots/automation.” If you wish to expound upon this project or want API access for another reason fill in the appropriate settings. Now you are going to need to describe your uses of the Twitter API. A little example pops up and blue and gives roughly what they’re looking for. 
•	Fill in the information using the reference pop-up.
•	select “NO” for the last question which is regarding government access to Twitter.
The screen will look like the image below.
 
Now onto the Terms of Service agreement. Be sure to read all of it in its entirety (who really does this, honestly?)
•	Now scroll down all the way in the window that displays the TOS document/agreement.
•	Click the top box that acknowledges you have read the agreement.
•	Click “Submit Application”
Now you will get an email to the address you have verified your twitter with. It will look like the image below. You want to click “Confirm Email”

 
 


Now the application you just submitted is under review. The time table on this varies. I just attempted to register 4 different accounts and within five minutes one got accepted, and as of this writing the others have not. Therefore, I have setup several applications in my Twitter Dev Environment so as a class we can use my access keys for this lab and you can substitute them out after you have received your own. I recommend maybe even creating a new email address for this project if you plan on doing more development projects. I personally have an email address just for development / API registration. It’s nice to have a separate entity just for these purposes. This may not be ideal for everyone and is therefore just an anecdote on personal experience. There are many other chatbot like applications you can build on a Raspberry Pi. To name a few:
•	Facebook Messenger Chatbot
•	Twitch Chatbot
•	Telegram Chatbot
•	Instagram bot / Moderator
•	Discord Bot / Moderator
These all require a similar setup to the one we just went through. You’re going to need to register for API access and therefore it can be handy having a separate email address just for these purposes. After several APIs and development projects it’s easy to lose track of what’s what. 

Step 3 : Find your API key
To access your API keys to list them in the file needed for the bot follow the instructions below.
•	You need to access your API keys. They are found on your main developer page. 
•	First go back to your browser window. 
•	Ensure you are at developer.twitter.com. 
•	Click “Developer” on the far top right. 
•	This is the main page. You should see your avatar icon in the top right of the page. 
•	Just to the left is the name of the app your setup. Click this to get further details. 
•	Then click “Apps” Then you will see your apps displayed. 
•	Click “Details” on the right side.
•	Once there you need to click “Keys and Tokens” at the top nav bar. It is between App Details and Permissions


 

 


 



 


Step 4: Setting up your application:

 
This may change if Twitter changes their application protocol, but here's the procedure for the time being:
Go to https://apps.twitter.com/ and click on Create New App
At the Create an Application dialog box, enter:
- Name of your application
- Description
- Link to valid URL (this can be changed later)
Leave the Callback URL Read the terms of agreement and agree to them and then OK the dialog
Step 6: Modify Permissions for Read/write

 
Twitter will take you to a page for Application Settings (I blacked out my API key for security reason).The first thing you'll need to do is change the permission, click on modify permissions on the Access level tab. Choose either Read and Write or Read, Write and Access direct messages, the latter if your Twitterbot will parse DMs. Click on Update Settings. If you get the error that you need to add your mobile phone to your account, then you probably skipped the "Add mobile phone to account" step of this tutorial. Click on the Details tab and then you're back at the Application Settings dialog. Wait for a minute and click on Refresh until your Access level changes to Read/Write.
Step 7: Get Access Token and API Keys

Click on the API Keys Tab, and you will see a dialog with your API keys. What we want to do now is create your Access Token. Click on the Create Access Token button and you will be given an Access 
Step 8: Delete Your Mobile Phone Number from the Account

We don't need the mobile phone number on your Twitter account, so go back to this screen and choose Delete phone






Project Stage: 2
Step 0: So…A bot?
Welcome! Either you have just setup your own developer account with twitter, or you have chosen to use the accounts and credentials provided. (*These credentials will be reset after presentation so if you enjoy this project please continue with your own access!*)
There are so many possibilities with the Twitter API. Bots are by far the most popular usage by the public today. Bots can literally be created in an unlimited number of ways. From hard-coding the bot instructions (what we’re doing here,) setting up a single Google doc file, to serverless scripts on hosting providers like Heroku. Anyone can create a bot with any number of utility and functionality and purposes. Some common uses people use are tweeting about the weather, tweeting when a specific account updates, and herding mass followers. Our bot will serve to automatically tweet on its own and interact with other users on a minimal basis. However, we will show some of the more advanced and powerful options in case you’re interested in trying them yourself later. 

The possibilities with the API access is literally limitless. You have access to so much information regarding the authorized account, and other twitter users as well. We are only going to scratch the surface in this lab, but we will be sure to include some cool examples for you to try another time.

When it comes to working with the API we have a few different options. We can use the syntax of the API itself or choose from hundreds of different libraries in dozens of languages. Seeing that we’re working with the Pi Python seems like an obvious choice. Now that we’ve narrowed down our choices we still have a plethora of options to choose from. When it comes to Python Libraries for the Twitter API there are two front-runners: Tweepy & Twython. We are going to work with Tweepy in this lab.

Step 1: Setting up your environment
It’s a good idea to run updates first. Copy and paste the following commands one at a time – most will require confirmation.
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install python-pip (this will take a minute)
pip is a package manager for Python. It is system independent and connects to Python Package Index and downloads, then installs the packages. (sudo is not always needed when using pip, however I use it every time out of habit)
sudo pip install tweepy
sudo pip install setuptools
Tweepy lets you use the Twitter API through Python. It depends on the setuptools library to work properly. The urllib2 and json libraries should be included by default, but to check for them, type the following:

pip list
if you see urllib – great, if not – just use pip install urllib3.
Now we are ready to begin coding bots. You can copy the code from this document or download it from the link provided. 
begin by making a new directory to house your Tweet project, then create a new file.
Sudo mkdir twitterBot
cd twitterBot
sudo nano credentials.py
It’s very important that the file be named “credentials.py” as it is how we will continue to access the API. Copy the below code into this newly created file and save it. You are also welcome to download the file directly.
# Credentials for your Twitter bot account

# 1. Sign into Twitter or create new account
# 2. Make sure your mobile number is listed at twitter.com/settings/devices
# 3. Head to apps.twitter.com and select Keys and Access Tokens
# 
#If you are using the example account provided copy the following API keys.
#Ensure they are in a file called "credentials.py" It's very important that the file name is exact.
#
CONSUMER_KEY = '6gTma2ITYHEh7MZMRJaflnxK7'
CONSUMER_SECRET = 'a20hHEbN1qudaR6RAdMCHtPKdOjpjiiNKabXjhj52Ajb4uHz2S'

# Create a new Access Token
ACCESS_TOKEN = '1051987549487534081-quzVSEUw33JJiImQ7mSnyvZvdTsmln' 
ACCESS_SECRET = 'Uz5w4bC3heTN3efnA5yuh7lOZZMzYzkZYThykqRgnZUtu'
Now, ensure we are in the correct directory with the command pwd. It should look like this: /home/pi/twitterbot
Now, on to the file “basicbot.py” If you have not downloaded the files all together either go and fetch this one, or we will create it now together. 
Step 2: Starting the code / Bot 1

sudo nano basicbot.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This bot tweets three times, waiting 15 seconds between tweets.

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/@CSCC_Linux_Bot

# Housekeeping: do not edit!
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot will tweet
tweetlist = ['Test tweet one for XXX !', 'Test tweet two for XXX!']

for line in tweetlist: 
    api.update_status(line)
    print line
    print '...'
    time.sleep(15) # Sleep for 15 seconds

print "All done!"
Now go ahead and change the two occurrences of “XXX” you see to a variant of your name. Pinkerman, mpink, mikep, MIP, etc. will all work just fine. This is so you can verify your tweets are going through, since we have multiple users interacting with the same account. The bot will send out three tweets, at regular intervals. These tweets are pre-defined “strings.” Strings in Python are enclosed in single or double quotes. In this case, the strings are specified as a “list”— designated by square brackets in Python — and this list is assigned to the variable tweetlist. Modifying the strings will alter what the bot tweets. The list of strings can be modified or shortened. However, running this script repeatedly without changing it will present error messages, because the Twitter API will not allow re-posting of identical tweets.
Now time to execute our bot script! Issue the following command: (RED TEXT)
pi@raspberrypi:~/twitterbot $ python ./basicbot.py		
You should now see the print commands on the terminal window: 
“Test tweet one for XXX!
…
Test tweet two for XXX!
…
All done!”
Now check the twitter feed of @CSCC_Linux_Bot (Or if you’re currently expanding your horizons and giving in into that itching curiosity – your own account!) to see your tweets! If you got any errors in response, feel free to search the error on Stack Overflow or ask for assistance.
Let’s up the complexity here. The capabilities of API access are crazy. Let’s try some new things out now. If you have downloaded the files directly we are now going to address “rando_bot1.py” If you are following along / copy + pasting your way through you will find the code below. So now we are going to introduce Python’s capabilities to read files that are stored elsewhere and then use that data. I have created several variants of this bot. I will show and link to all of them, but we are going with the most straightforward/simple one for our walkthrough as a class. If you have not downloaded the files all together either go and fetch this one, or we will create it now together. 
Step 3: Implementing some complexity to our code / Bot 2

sudo nano rando_bot.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bot Tutorial Step 2 / bot number 2

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/@CSCC_Linux_Bot

# This bot tweets a random line from a text file. There are some very cool
# ways to use this capability and I will outline a few after this initial setup

import tweepy, time
from credentials import *
from random import randint

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot will tweet…
# MAKE SURE YOU PUT THE CORRECT FILENAME BELOW!!!
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
So, in the middle of this file you will see the line of code:
filename = open('userchoice.txt','r') 
(If you have downloaded the files skip to step 2) Now we are going to create a blank text file. Ensure it has the same name as the line of code shown above (extension and ALL!)
sudo nano userchoice.py
If you are following along skip the first 20 lines when copying to your file. You need line 22-32. 

Below you will find random sentences (some chosen by me, some generated by a bot) to illustrate the randomness we are implementing into our bot. You need to replace all occurrences of "XXXX" with your initials or some variant of your name.

Just use sed to do it quickly. 
Don't know what that is? 
Well just read on and you'll learn something new!

BONUS LESSON!
Did you know there is a command line utility for just this purpose! Its sed. Follow the instructions below to find + replace within this document

sed -i 's/original/new/g' file.txt

Explanation:

sed = Stream EDitor
-i = in-place (i.e. save back to the original file)
The command string:

s = the substitute command
original = a regular expression describing the word to replace (or just the word itself)
new = the text to replace it with
g = global (i.e. replace all and not just the first occurrence)
Copy this code for your userchoice.txt file.
My name is XXXX, and im tweeting from an API right now!
Hi, I am XXXX and I am building a bot at this very moment!
I like turtles. Don't believe me? Ask my mom XXXX.
XXXX is king of the russian bots!
XXXX voted for Donald Trump!
A purple pig and a green donkey flew a kite with XXXX in the middle of the night and ended up sunburnt.
When I, XXXX, was little I had a car door slammed shut on my hand. I still remember it quite vividly.
Is it free? Asked XXXX repeatedly.
The clock within this blog and the clock on my laptop are 1 hour different from each other exclaimed XXXX.
The lake is a long way from here shouted XXXX
Now use the sed command we just discussed to make it personal.
pi@raspberrypi:~/twitterbot $ sed -i 's/XXXX/MIP/g' userchoice.txt
Open the file in nano to ensure the changes have been made.
Now execute this bot the same way we did the last one
pi@raspberrypi:~/actualbot $ sudo python ./rando_bot.py
Hi, I am XXXX and I am building a bot at this very moment!
You can see the response I got when issuing the command above. If all went according to plan you should see one of the random ten sentences you just edited. Go verify that it was tweeted.

Step 2b: Bonus – Some additional uses / functionality with concepts we just learned.
I mentioned some cool uses for this and promised to show you one/some. We will not be doing this one together but feel free to try it later. We are going to use some of the very same code, but we are going to make some changes. If you’re going off downloads this is reader_bot.py. What we are going to do is change the bot, so it doesn’t just grab random lines, but starts from line 1 and keeps progressing. A common usage is to download a book in .txt format and have the bot tweet it line by line over time. Here is the code:
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/@CSCC_Linux_Bot

# This bot tweets a text file line by line, waiting a
# given period of time between tweets.

# Download a Project Gutenberg "Plain Text UTF-8" file,
# open it in Notepad, remove junk at beginning,
# and replace all double-linebreaks with single linebreaks.

# Housekeeping: do not edit
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot will tweet
filename = open('data/dorian_grey.txt', 'r')
tweet_text = filename.readlines()
filename.close()

# loop through the tweet_text
for line in tweet_text[0:5]: # Will only write first 5 lines
    api.update_status(status=line)
    print(line)
    time.sleep(15) # Sleep for 15 seconds

print("All done!")

Step 2c: Bonus – Some additional uses / functionality with concepts we just learned.
Let’s look to what else we can do with the Twitter API. The twitter API also gives you a great deal of access to other users and their activity. We are going to briefly cover setting up some automation, I mean this is a “bot” after all. We are not going to do this all together because it would cause a lot of chaos if multiple tweets were set to go out at once from multiple places. Going off the code we just used we can make a few adjustments and have real-time interaction completely automated.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This bot listens to the account @realdonaldtrump, and when that account
# tweets, it responds with a line of Twain

# Download a Project Gutenberg "Plain Text UTF-8" file,
# open it in Notepad, remove junk at beginning,
# and replace all double-linebreaks with single linebreaks.

# Housekeeping: do not edit
import tweepy
import time
from credentials import *
from random import randint
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# initially, the script will assume that the last tweet was a null value
last_tweet = None

# What the bot will tweet
filename = open('data/twain.txt', 'r')
tweet_text = filename.readlines()
filename.close()

# a function that picks a random line
def line_number():
    return randint(0, len(tweet_text) - 1)

# this is the function that does most of the work of the bot
def compare_tweets():

    # uses the global lasttweet variable, rather than the local one.
    # (it's probably best practice not to use a global variable for
    # this purpose, but we've shown this approach for its readability.)
    global last_tweet

    # gets the most recent tweet by @realdonaldtrump and prints its id
    most_recent_tweet = api.user_timeline('realdonaldtrump')[0]
    print(most_recent_tweet.id)

    # compares the two tweets, and tweets a line of Twain
    # if there is a new tweet from @realdonaldtrump
    if most_recent_tweet != last_tweet:
	# line = “@realdonaldtrump ” + tweettext[linenum()] – This will make the response tweet directly at the user the bot is listening to.


        line = tweet_text[line_number()]
        api.update_status(status=line)
        print(line)

    # updates last_tweet to the most_recent_tweet

    last_tweet = most_recent_tweet

# runs the compare_tweets function every 5 seconds
while True:
    compare_tweets()
    print("sleeping")
    time.sleep(5)  # Sleep for 5 seconds

# To quit: CTRL+C and wait a few seconds
So now we have added the function “compare_tweets.” The code goes out to the account you select (yes, we put Donald Trump because if it tweets when they do, might as well make it active and interesting.) and it pulls the most recent tweet with the global variable, it then gets the most recent by the user’s timeline. Then the code compares the two and if they are different the bot will tweet.
Step 3: Something that serves some “purpose” and meets the “bot” qualifications
So, we’ve discussed the Twitter API, how it’s used, and only scratched the surface of its capabilities. We will include various ‘bonus’ materials if you’d like to follow up. One ‘nifty’ example is a bot that searches Twitter for contest being held that require interaction. This bot finds these contests and it enters them automatically. Let’s get to our “bot” for now. If you’ve downloaded the files this is the ‘otdbot.py’ we are discussing now. First ensure you are still in the same directory 
/home/pi/twitterbot

sudo nano otdbot.py

import tweepy # for tweeting
import Wikipedia # to parse data from Wikipedia
import datetime # to get date; actual wiki page has more info than "on this day"
import random
from credentials import *

def get_date():
    """ returns today's date as string, e.g. 'January 01' """
    today = datetime.date.today() # ex 2015-10-31
    return today.strftime("%B %d")

def get_event():
    """ returns a string 140 characters or less of a random Events item """
    this_day = wikipedia.page(get_date())
    events = this_day.section("Events") # unicode
    # split unicode into list items
    lines = events.split('\n')
    # get random item in list
    item_index = random.randrange(len(lines))
    event_text = lines[item_index]
    # tweet the whole sentence if it's short enough
    if len(event_text) <= 140:
        return event_text
    # otherwise just print the first 137 characters plus "..." = 140
    else:
        return event_text[0:137] + "..."

def tweet(message):
  

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    print("TWEETING! ".format(message))
    api.update_status(status=message)
    """ Send tweet """
 

tweet(get_event())
This bot uses a few different libraries we haven’t used yet. To make things easier they are included in “requirements.txt” All you must do is type
pip install -r requirements.txt
This bot uses Wikipedia to find an interesting fact about the current date. It then composes a tweet from this text and tweets it automatically, neat right? Now let’s move on to making it 100% automatic.
Step 4: Automation in Linux
If we want to make any of our bots automatic, or any script really, we are going to use Cron. In Linux, Cron is a daemon/service that executes shell commands periodically on a given schedule. Cron is driven by a crontab, a configuration file that holds details of what commands are to be run along with a timetable of when to run them.
Start by entering the following command:
crontab -e
Entering the above command will open a terminal editor with a new blank crontab file, or it will open an existing crontab if you already have one. You can now enter the commands to be executed
A crontab file has six fields for specifying minute, hour, day of month, month, day of week and the command to be run at that interval. See below:
*     *     *     *     *  command to be executed
-     -     -     -     -
|     |     |     |     |
|     |     |     |     +----- day of week (0 - 6) (Sunday=0)
|     |     |     +------- month (1 - 12)
|     |     +--------- day of month (1 - 31)
|     +----------- hour (0 - 23)
+------------- min (0 - 59)

To list existing entries, enter the following terminal command:
crontab -l

A double-ampersand && can be used to run multiple commands consecutively. The following example would run command_01 and then command_02 once a day:
@daily command_01 && command_02

To remove your crontab file simply enter the following terminal command:
crontab -r

Writing a crontab file can be a somewhat confusing for first time users, therefore I have listed below some crontab examples:
* * * * *  #Runs every minute
30 * * * *  #Runs at 30 minutes past the hour
45 6 * * *  #Runs at 6:45 am every day
45 18 * * *  #Runs at 6:45 pm every day
00 1 * * 0  #Runs at 1:00 am every Sunday
00 1 * * 7  #Runs at 1:00 am every Sunday
00 1 * * Sun  #Runs at 1:00 am every Sunday
30 8 1 * *  #Runs at 8:30 am on the first day of every month
00 0-23/2 02 07 *  #Runs every other hour on the 2nd of July
There is also a website that will generate the entries for you:
https://crontab-generator.org/
The best option for our last bot would be once a day:
@daily  #Runs once a day [0 0 * * *]

 
Conclusion
Congratulations, you have just successfully created a bot on Twitter! It was hard selecting what exactly to cover for this tutorial as there are just so many cool possibilities. As promised we will include some additional API uses, some existing cool bots, and a few other things we just don’t have the time to cover in class. All of these additional examples can be found in the same links provided for the previous bots. Your welcome to try these anyway you would like, and it’s also encouraged that you customize them to fit your needs or preferences. These “Bonus Bots” will be covered in a similar fashion to the above bots. The code will be shown here, along with the instructions on setting them up. They will also increase in complexity and difficulty as the others have done also. There will be some resources that will be included in the online repositories but they won’t be outlined here. Some are just simple examples I find interesting and don’t require explanation, others are beyond the scope of anything covered. For example, using the API for analytical purposes and/or data harvesting can get extremely complicated. 

Bonus Bot #1: Custom Text OR your CPU temperature 

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

This bot scripts serves two functions. The line of code :
if len(sys.argv) >= 2:        # use entered text as tweet  
    tweet_text = sys.argv[1]  
    print ' Tweeting: ' + tweet_text
 Serves to allow for custom messages. The variable sys.argv[1] allows you to type after the execution command to force tweet a message. If a message is not supplied then the raspberry pi will tweet it’s CPU temperature.

pi@raspberrypi:~/actualbot $ sudo python ./pitemp.py "Hello There Fellow Bots!"
 Tweeting: Hello There Fellow Bots!
pi@raspberrypi:~/actualbot $ sudo python ./pitemp.py
2018/10/26 21:55:17 Pi Processor Temperature is 51.5 °C
pi@raspberrypi:~/actualbot $

As you can se above, if input is supplied it is passed as “tweet_text” and will be the body of the tweet. If none is passed you are given the CPU temp.

 

And above, you see the tweets were tweeted accordingly.










Bonus Bot #2: Tweeting pictures from a folder 

import tweepy  
from subprocess import call  
from datetime import datetime  
from credentials import *
  
i = datetime.now()               #take time and date for filename  
now = i.strftime('%Y%m%d-%H%M%S')  
photo_name = now + '.jpg'  
cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name   
call ([cmd], shell=True)         #shoot the photo  
  
# Consumer keys and access tokens, used for OAuth  
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
  
# Send the tweet with photo  
photo_path = '/home/pi/' + photo_name  
status = 'Photo auto-tweet from Pi: ' + i.strftime('%Y/%m/%d %H:%M:%S')   
api.update_with_media(photo_path, status=status) 

In the above example we are tweeting a photo and not just text. With the raspberry pi you can write scripts that will utilize your webcam, take a photo, overlay text and graphics, then tweet them. This is just tweeting a photo that is already saved in a folder. 


Now let’s look at fetching data with our API access. Twitter is the chosen medium to experiment on for a lot people who want to learn data science. The API of the platform is well documented and clear. Most programming languages have good libraries for interfacing with it. And, finally, Twitter data is much more straightforward to process than, for instance, Facebook data. 

You can stream large amounts of data instantly with API access and the possibilities are just limitless. If you were to implement the streaming API with Python it would look something like this:









Bonus Bot #3: Using the stream API to get user tweets 



#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1051987549487534081-quzVSEUw33JJiImQ7mSnyvZvdTsmln"
access_token_secret = "Uz5w4bC3heTN3efnA5yuh7lOZZMzYzkZYThykqRgnZUtu"
consumer_key = "6gTma2ITYHEh7MZMRJaflnxK7"
consumer_secret = "a20hHEbN1qudaR6RAdMCHtPKdOjpjiiNKabXjhj52Ajb4uHz2S"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Trump', 'Hillary', 'Warren'])


You can see the API keys are right in the code and not imported from another file as we have been doing. This is simply because this was created outside that directory and I decided to take a shortcut. Either way works but the way we have been doing it is far better as your valuable keys aren’t out in the open as much.



 

This is what the terminal window looks like when you run the streaming API via Python. It’s a lottttttt. You can carrot the output to a new file like sudo python ./stream.py > twitter_data.txt. Then you can analyze the data later on. You can write scripts in Python to sort the data and extract the fields you’d like to work with.



 

A quick example of what we can do…



import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from credentials import *
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
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
twitter_stream.filter(track=['#Trump'])

Above we use our API to stream active tweets across twitter. It can be a lot to see such a thing. Let’s search all of twitter for the hashtag ‘#Trump’ and see what we can find.

We let the script run for a few minutes and cancelled it with CTRL + C. Now a new file has been created called FILENAME.json.
 


 

A huge .JSON file full of our hashtag #Trump. There is a plethora of data for each tweet, and there are a lot of tweets in a just a short amount of time. I want to find the location of each tweet. Out of the multitude of information stored in the tweet, I want to access location data for the tweet itself, and if that isn’t available, the user. I wrote the following script to do this:

import json
# Tweets are stored in in file "fname". In the file used for this script, 
# each tweet was stored on one line
fname = 'FILENAME.json'
with open(fname, 'r') as f:
    
    #Create dictionary to later be stored as JSON. All data will be included
    # in the list 'data'
    users_with_geodata = {
        "data": []
    }
    all_users = []
    total_tweets = 0
    geo_tweets  = 0
    for line in f:
        tweet = json.loads(line)
        if tweet['user']['id']:
            total_tweets += 1 
            user_id = tweet['user']['id']
            if user_id not in all_users:
                all_users.append(user_id)
                
                #Give users some data to find them by. User_id listed separately 
                # to make iterating this data later easier
                user_data = {
                    "user_id" : tweet['user']['id'],
                    "features" : {
                        "name" : tweet['user']['name'],
                        "id": tweet['user']['id'],
                        "screen_name": tweet['user']['screen_name'],
                        "tweets" : 1,
                        "location": tweet['user']['location'],
                    }
                }
                #Iterate through different types of geodata to get the variable primary_geo
                if tweet['coordinates']:
                    user_data["features"]["primary_geo"] = str(tweet['coordinates'][tweet['coordinates'].keys()[1]][1]) + ", " + str(tweet['coordinates'][tweet['coordinates'].keys()[1]][0])
                    user_data["features"]["geo_type"] = "Tweet coordinates"
                elif tweet['place']:
                    user_data["features"]["primary_geo"] = tweet['place']['full_name'] + ", " + tweet['place']['country']
                    user_data["features"]["geo_type"] = "Tweet place"
                else:
                    user_data["features"]["primary_geo"] = tweet['user']['location']
                    user_data["features"]["geo_type"] = "User location"
                #Add only tweets with some geo data to .json. Comment this if you want to include all tweets.
                if user_data["features"]["primary_geo"]:
                    users_with_geodata['data'].append(user_data)
                    geo_tweets += 1
            
            #If user already listed, increase their tweet count
            elif user_id in all_users:
                for user in users_with_geodata["data"]:
                    if user_id == user["user_id"]:
                        user["features"]["tweets"] += 1
    
    #Count the total amount of tweets for those users that had geodata            
    for user in users_with_geodata["data"]:
        geo_tweets = geo_tweets + user["features"]["tweets"]
    #Get some aggregated numbers on the data
    print "The file included " + str(len(all_users)) + " unique users who tweeted with or without geo data"
    print "The file included " + str(len(users_with_geodata['data'])) + " unique users who tweeted with geo data, including 'location'"
    print "The users with geo data tweeted " + str(geo_tweets) + " out of the total " + str(total_tweets) + " of tweets."
# Save data to JSON file
with open('Blackstone_users_geo.json', 'w') as fout:
    fout.write(json.dumps(users_with_geodata, indent=4))

 

After running the script we get the following output above. We have 60 users and their locations now in JSON format. Below is a screenshot of the new file opened in VisualStudio.
 

So what to do with this data now? Well we can use our geo-json data points to plot a map, make a graph, or run data analysis on location-based tweeting. When configuring this data to be formatted differently it starts to look more readable.

 

Now we can use a library like matplotlib or a service like carto to plot these geo points (after we utilize the Google Maps API to reverse-geo-code the location points pulled with the python script.)

