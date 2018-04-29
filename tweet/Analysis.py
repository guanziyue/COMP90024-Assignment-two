from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import re
from profanity import profanity
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
# analyze sentiment. input is string,return a dictionary including pos: postive probability.
#neg: negative probability. compoud: when positive int, positive, negtive int ,negative. zero, neutual
def sentiment_analysis(content):
    senti_analyzer=SentimentIntensityAnalyzer()
    return senti_analyzer.polarity_scores(content)

# check if the sentence have a profanity word.
def profanity_analysis(content):
    content=re.sub(r'#(\w+)\b',' $1 ',content)
    content=re.sub(r'@\w+\b','',content)
    tokens=nltk.word_tokenize(content.lower())
    contain_profanity=profanity.contains_profanity(content)

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