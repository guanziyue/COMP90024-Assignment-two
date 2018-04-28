import tweepy
import json
import couchdb

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


# My keys and tokens
consumer_key = 'UjnHPModDzohpESefLeSCncAk'
consumer_secret = '2OWQ9zYinzMZB3gUQx3o3tfIdt0JX2x00hRoBJqcxBN9I5E4nv'
access_token = '988327751126925312-ts0LnQL22Cb1IOPnrHyobyu6BVWjTsO'
access_token_secret = '9aRnHHOcLwVsHfw2264JebZQExWZKAZAxW2b6eOKGLF5D'

# Save JSON file to the text file

#tweets = open("try.txt","w")

#This is a basic listener that just prints received tweets to stdout.

class StdOutListener(StreamListener):

    def on_data(self, data):

        tweetdata = json.loads(data.encode('gbk'))
        id = tweetdata['id']
        text = tweetdata['text']
        place = tweetdata['place']['bounding_box']['coordinates']

        print (place)
        #tweets.write(data)
        self.savetodb(data)
        #json.dump(tweetdata, tweets)

        return True

    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        print (status)

    def savetodb(self,data):
        address = "http://admin:admin@115.146.86.154:5984/"
        couch = couchdb.Server(address)
        try:
            db = couch.create('try') # create db
        except:
            db = couch['try'] # existing
        db.save(json.loads(data.encode('gbk')))

def getKeyToken():

    access = {"consumer_key": consumer_key,
            "consumer_secret": consumer_secret,
            "access_token": access_token,
            "access_secret": access_token_secret}

    auth = tweepy.OAuthHandler(access['consumer_key'], access['consumer_secret'])
    auth.set_access_token(access['access_token'], access['access_secret'])
    return auth

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API

    listener = StdOutListener()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(getKeyToken(), listener)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(locations = [144, -38, 145, -37])


tweets.close()