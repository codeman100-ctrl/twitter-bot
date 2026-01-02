import tweepy
from tweepy import OAuthHandler
import os
from dotenv import load_dotenv

load_dotenv()
    


client = tweepy.Client(consumer_key=os.getenv("CONSUMER_KEY"),
                       consumer_secret=os.getenv("CONSUMER_KEY_SECRET"),
                       access_token=os.getenv("ACCESS_TOKEN"),
                       access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
                       )

# auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)



# Source - https://stackoverflow.com/a
# Posted by Futurist Forever, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-01, License - CC BY-SA 4.0

# # Authenticate to Twitter
# client = tweepy.Client( 
#     consumer_key=CONSUMER_KEY,
#     consumer_secret=CONSUMER_KEY_SECRET,
#     access_token=ACCESS_TOKEN,
#     access_token_secret=ACCESS_TOKEN_SECRET
# )

# Post Tweet
message = "Hello World! This is my first tweet ussdgfdsging Tweepy in Python! #Tweepy #Python #TwitterAPI #HelloWorld "
client.create_tweet(text=message)
print("Tweeted!")
