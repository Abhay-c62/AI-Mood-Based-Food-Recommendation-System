import nltk

# Download VADER lexicon if not already present
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def detect_mood(text):

    text = text.lower()

    # Keyword-based detection
    if any(word in text for word in ["stress", "stressed", "pressure", "overwhelmed"]):
        return "Stressed"

    if any(word in text for word in ["angry", "mad", "furious", "annoyed"]):
        return "Angry"

    if any(word in text for word in ["excited", "thrilled", "amazing"]):
        return "Excited"

    if any(word in text for word in ["tired", "sleepy", "exhausted"]):
        return "Tired"

    if any(word in text for word in ["relaxed", "calm", "peaceful"]):
        return "Relaxed"

    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.5:
        return "Happy"
    elif compound <= -0.5:
        return "Sad"
    else:
        return "Neutral"