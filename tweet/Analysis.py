from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# analyze sentiment. input is string,
def sentiment_analysis(content):
    senti_analyzer=SentimentIntensityAnalyzer()
    return senti_analyzer.polarity_scores(content)

