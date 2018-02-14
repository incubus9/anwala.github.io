import tweepy
import time
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
consumer_key = "fAkotcp8vBt6cR3iLXLgppvIW"
consumer_secret = "pYMZVGBSUkwsnD8bw8goF22t1cFKm1AFk2xFWnL4OIGioCRvLW"
access_token = "913237521202638849-DqK1BQAH6CDHj5EINNPXbgJdmN3YdJS"
access_token_secret = "kDXDinKcG9MEX5CGLS8Hv0K0oSvAabSVmAVUlPcUjGGQS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

public_tweets = api.home_timeline()

file = open("input.txt","w")
class StreamObj(tweepy.StreamListener):
    a = 0
    inputList = []
    def on_data(self, data):
        count = 1000
        out = json.loads(data)
        try:
            if StreamObj.a >= count:
               return False

            else:
                for url in out["entities"]["urls"]:
                    StreamObj.a += 1
                    StreamObj.inputList.append(url["expanded_url"])
                    print(StreamObj.a)
                    
        except KeyError:
            print("data keys")
            print(data.keys())   

def checkURI(strObj = StreamObj()):
    for x in strObj.inputList:
        file.write(x+"\n")
        print(x)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
streamObj = StreamObj()
myStream = tweepy.Stream(auth = api.auth, listener=streamObj)

myStream.filter(track=['basketball'])

checkURI(streamObj)
