from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# analyze sentiment. input is string,return a dictionary including pos: postive probability.
#neg: negative probability. compoud: when positive int, positive, negtive int ,negative. zero, neutual
def sentiment_analysis(content):
    senti_analyzer=SentimentIntensityAnalyzer()
    return senti_analyzer.polarity_scores(content)

