import tweepy
import json
import re
import couchdb

import nltk
from profanity import profanity
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# My keys and tokens
consumer_key = 'tQXUrW8oFwCzOwBvVz58ESvJC'
consumer_secret = 'WIWzELsSyjUgfIqSYbBXwSbMPTOHFh11i9VQrfbSCni3SSXgts'
access_token = '990553108160761861-t3ygqAm46AkhchJP3smE52y2ovKdOgZ'
access_token_secret = '9zn4ToMWxAO146X0HwTcPdPt6BkKPDrjayIR2RPU40AJZ'

# Get the authentication
def getKeyToken():

    access = {"consumer_key": consumer_key,
            "consumer_secret": consumer_secret,
            "access_token": access_token,
            "access_secret": access_token_secret}

    auth = tweepy.OAuthHandler(access['consumer_key'], access['consumer_secret'])
    auth.set_access_token(access['access_token'], access['access_secret'])
    return auth


# check if the sentence have a alcohol name.
def beer_check(str):
    beerNames = ["alcoholic", "alcohol", "brewery", "beer", "wine", "shiraz", "cabernet", "sauvignon", "chardonnay",
                 "merlot", "semillon", "pinot", "noir", "riesling", "blanc", "4 Pines", "abbotsford invalid",
                 "ballarat bitter", "beaten track", "bluetongue", "boag's", "bootleg", "brisbane bitter", "broo",
                 "burleigh", "brewing", "carlton black", "carlton cold", "carlton draught", "carlton midstrength",
                 "cascade", "castlemaine brewery", "castlemaine perkins", "XXXX", "chopper", "crown lager", "pilsner",
                 "emu", "feral", "foster's", "gage roads", "peter grant", "hahn brewery", "hahn premium",
                 "hahn super dry", "holgate", "james boag's", "kalgoorlie", "kb", "lion", "little creatures",
                 "little world", "lobethal bierhaus", "malt shovel", "melbourne bitter", "mountain goat", "nail",
                 "nt draught", "pure blonde", "skinny blonde", "southwark bitter", "st arnou", "stone & wood",
                 "thunder road", "tooheys", "vb", "victoria bitter"]

    check = False
    for name in beerNames:
        if name in str:
            check = True
            break
    return check

# analyze sentiment. input is string,return a dictionary including pos: postive probability.

#neg: negative probability. compoud: when positive int, positive, negtive int ,negative. zero, neutual

def sentiment_analysis(content):

    senti_analyzer=SentimentIntensityAnalyzer()
    return senti_analyzer.polarity_scores(content)



# check if the sentence have a profanity word.
def profanity_analysis(content):
    content=re.sub(r'#(\w+)\b',' $1 ',content)
    content=re.sub(r'@\w+\b','',content)
    #tokens=nltk.word_tokenize(content.lower())

    contain_profanity=profanity.contains_profanity(content)

    return contain_profanity



# check if the word is relevant to crime

def check_crime(word):

    max=0

    lemmatizer = WordNetLemmatizer()
    word_n = lemmatizer.lemmatize(word, 'n')

    for synset in wn.synsets(word_n,'n'):
        if max<synset.wup_similarity(wn.synset("crime.n.01")):
            max=synset.wup_similarity(wn.synset("crime.n.01"))

        if max<synset.wup_similarity(wn.synset("crime.n.02")):
            max=synset.wup_similarity(wn.synset("crime.n.02"))

        if max<synset.wup_similarity(wn.synset("assault.n.01")):
            max=synset.wup_similarity(wn.synset("assault.n.01"))

        if max<synset.wup_similarity(wn.synset("robbery.n.01")):
            max=synset.wup_similarity(wn.synset("robbery.n.01"))

        if max<synset.wup_similarity(wn.synset("fraud.n.01")):
            max=synset.wup_similarity(wn.synset("fraud.n.01"))

        if max<synset.wup_similarity(wn.synset("arson.n.01")):
            max=synset.wup_similarity(wn.synset("arson.n.01"))

        if max<synset.wup_similarity(wn.synset("extortion.n.01")):
            max=synset.wup_similarity(wn.synset("extortion.n.01"))

        if max<synset.wup_similarity(wn.synset("larceny.n.01")):
            max=synset.wup_similarity(wn.synset("larceny.n.01"))

    word_v = lemmatizer.lemmatize(word, 'v')

    for synset in wn.synsets(word_v, 'v'):
        if max < synset.wup_similarity(wn.synset("rob.v.01")):
            max = synset.wup_similarity(wn.synset("rob.v.01"))

        if max<synset.wup_similarity(wn.synset("assault.v.01")):
            max=synset.wup_similarity(wn.synset("assault.v.01"))

        if max<synset.wup_similarity(wn.synset("rob.v.01")):
            max=synset.wup_similarity(wn.synset("rob.v.01"))

        if max<synset.wup_similarity(wn.synset("extort.v.01")):
            max=synset.wup_similarity(wn.synset("extort.v.01"))

        if max<synset.wup_similarity(wn.synset("murder.v.01")):
            max=synset.wup_similarity(wn.synset("murder.v.01"))

    return max





def crime_analysis(content):

    content = re.sub(r'#(\w+)\b', ' $1 ', content)
    content = re.sub(r'@\w+\b', '', content)
    tokens = nltk.word_tokenize(content.lower())

    max=0.0

    for token in tokens:
        if max<check_crime(token):
            max=check_crime(token)

    if max>0.8:
        return True
    else:
        return False



def removehttp (tweetdata):

    try:
        text = tweetdata['extended_tweet']['full_text']

    except:
        text = tweetdata['text']

    pattern = re.compile('https://t.co/\w+')

    pat = pattern.findall(text)
    #print (pat)
    #print (text)
    if len(pat) is 1:
        aa = pat[0]
        text = text.replace(aa, "")


    return text


def add_id(tweetdata):
    id=tweetdata['id']
    tweetdata['_id']=str(id)
    return tweetdata


# Tweet listener
class tweetListener(StreamListener):

    def on_data(self, data):

        tweetdata = json.loads(data.encode('gbk'))
        tweetdata = add_id(tweetdata)

        tweetReal = removehttp(tweetdata)
        #print (tweetReal)

        tweetid = tweetdata['id']
        print (tweetid)
        # Call analysis functions
        sentiment = sentiment_analysis(tweetReal)
        beer = beer_check(tweetReal)
        profanity = profanity_analysis(tweetReal)
        crime = crime_analysis(tweetReal)


        # Print
        #print (sentiment)
        #print (beer)
        #print (profanity)
        #print (crime)


        # Update
        tweetdata['sentiment'] = sentiment
        tweetdata['beer'] = beer
        tweetdata['profanity'] = profanity
        tweetdata['crime'] = crime


        tweetsave = json.dumps(tweetdata)
        self.savetodb(tweetsave)
        self.savetodb(tweetsave)

        return True

    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        print (status)

    def savetodb(self,data):
        address = "http://admin:admin@115.146.86.154:5984/"
        couch = couchdb.Server(address)
        try:
            db = couch.create('truetweet') # create db
        except:
            db = couch['truetweet'] #



        try:
            db.save(json.loads(data.encode('gbk')))
        except:
            pass


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API

    listener = tweetListener()
    stream = Stream(getKeyToken(), listener)

    # Only search tweets in restricted area
    stream.filter(locations = [150.4, -34, 151.2, -33])

tweets.close()