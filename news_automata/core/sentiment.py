from textblob import TextBlob

def sentiment(text):
    """
    Sentiment for a text.

    Polarity: [-1, 1]
    Subjectivity: [0, 1]
    """
    t = TextBlob(text)
    s = t.sentiment
    return s.polarity, s.subjectivity
