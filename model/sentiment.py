from textblob import TextBlob

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

    # Sentiment Analysis using TextBlob
    polarity = TextBlob(text).sentiment.polarity

    if polarity >= 0.5:
        return "Happy"
    elif polarity <= -0.5:
        return "Sad"
    else:
        return "Neutral"