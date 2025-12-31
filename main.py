import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'yNF6OETcqLonPdTL10KZZX4L0'
CONSUMER_KEY_SECRET = 'YCbcLTDBuMFirQuKc0zakEaFCOCU93kTNFt5IWnpkdQsccJple'
ACCESS_TOKEN = '1273630329249705986-3Rq63Nk96O0p5R0uYkUmW6FS4WvD94'
ACCESS_TOKEN_SECRET = 'cSnCmEGPIlweprCdNX6ame2uZALqz1DeTh1QyGKwVzMPO'

client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_KEY_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET,
                       bearer_token='AAAAAAAAAAAAAAAAAAAAAGc76gEAAAAA1Dmn6vPUXEZwFkdrzyhom6cDOtE%3DddECW6DjDaZRlMT61C7xNvoy6HwoD0QpFXR5fOaM8ow7O6Mftl')

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
