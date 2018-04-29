import tweepy
import json
import re
import couchdb

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


# My keys and tokens
consumer_key = 'UjnHPModDzohpESefLeSCncAk'
consumer_secret = '2OWQ9zYinzMZB3gUQx3o3tfIdt0JX2x00hRoBJqcxBN9I5E4nv'
access_token = '988327751126925312-ts0LnQL22Cb1IOPnrHyobyu6BVWjTsO'
access_token_secret = '9aRnHHOcLwVsHfw2264JebZQExWZKAZAxW2b6eOKGLF5D'

# Get the authentication
def getKeyToken():

    access = {"consumer_key": consumer_key,
            "consumer_secret": consumer_secret,
            "access_token": access_token,
            "access_secret": access_token_secret}

    auth = tweepy.OAuthHandler(access['consumer_key'], access['consumer_secret'])
    auth.set_access_token(access['access_token'], access['access_secret'])
    return auth


def userLang (tweet):
    return tweet['user']['lang']

def tweetLang (tweet):
    return tweet['lang']

def removehttp (text):
    pattern = re.compile('https://t.co/\w+')

    pat = pattern.findall(text)
    print (pat)
    print (text)
    if len(pat) is 1:
        aa = pat[0]
        print (text.replace(aa, ""))






# Tweet listener
class tweetListener(StreamListener):

    def on_data(self, data):

        tweetdata = json.loads(data.encode('gbk'))

        # id = tweetdata['id']

        try:
            text = tweetdata['extended_tweet']['full_text']
            print("1")
        except:
            text = tweetdata['text']





        # place = tweetdata['place']['bounding_box']['coordinates']


        user_lang = userLang(tweetdata)
        tweet_lang = tweetLang(tweetdata)


        tweetdata['user_lang'] = user_lang
        tweetdata['tweet_lang'] = tweet_lang

        removehttp(text)


        try:
            coord = tweetdata['coordinates']['coordinates']
            print (coord)
        except:
            pass




        tweetsave = json.dumps(tweetdata)
        self.savetodb(tweetsave)
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


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API

    listener = tweetListener()
    stream = Stream(getKeyToken(), listener)

    # Only search tweets in restricted area
    stream.filter(locations = [144, -38, 145, -37])

tweets.close()