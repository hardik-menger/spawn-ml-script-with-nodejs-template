import pandas as pd
import sklearn as skl
import numpy as np
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


CONSUMER_KEY = 'gejfWul5iUg3qKQfSDiYzvkyn'
CONSUMER_SECRET = 'pu0YscYt1vJvKS714fnMRL8oxC1NGpvzjXT1hVyfJ6X6WuE7NC'
ACCESS_KEY = '1027969527714336768-d9zUk6g67A1B6yve4ZZ6QIqD5mDtic'
ACCESS_SECRET = 'FP2nrfJ7v7NHezSvt9u1uR6YoHgPnmm6ip0mALUprTYrB'

class TweetListener(StreamListener):
    # A listener handles tweets are the received from the stream.
    #This is a basic listener that just prints received tweets to standard output

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitterStream = Stream(auth,TweetListener())

if(api.verify_credentials):
    print ('We successfully logged in')



user = api.get_user(name)



# predict the response for a new observation
VAL = knn.predict([[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P]])

if(VAL==1):
  print("User is GENUINE")
else:
  print("User is FAKE")





