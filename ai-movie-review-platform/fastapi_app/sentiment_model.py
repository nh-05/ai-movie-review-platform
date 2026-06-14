"""
sentiment_model.py – Sentiment prediction using TextBlob
Falls back to keyword-based analysis if TextBlob not available.
"""

import os
import pickle

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'sentiment.pkl')


def predict_sentiment(text: str) -> tuple[str, float]:
    """
    Predict sentiment of text.
    Returns (sentiment_label, confidence_score)
    sentiment_label: 'Positive' | 'Negative' | 'Neutral'
    confidence_score: 0.0 – 1.0
    """
    # Try loading a pre-trained sklearn model first
    if os.path.exists(MODEL_PATH):
        try:
            return _predict_sklearn(text)
        except Exception:
            pass

    # Fall back to TextBlob
    try:
        return _predict_textblob(text)
    except ImportError:
        pass

    # Final fallback: keyword-based
    return _predict_keywords(text)


def _predict_textblob(text: str) -> tuple[str, float]:
    """TextBlob-based sentiment analysis."""
    from textblob import TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1.0 to 1.0

    if polarity > 0.1:
        return 'Positive', min(0.99, 0.5 + polarity * 0.5)
    elif polarity < -0.1:
        return 'Negative', min(0.99, 0.5 + abs(polarity) * 0.5)
    else:
        return 'Neutral', 0.5 + abs(polarity)


def _predict_sklearn(text: str) -> tuple[str, float]:
    """Sklearn-based sentiment analysis using pre-trained model."""
    with open(MODEL_PATH, 'rb') as f:
        model_data = pickle.load(f)

    vectorizer = model_data['vectorizer']
    classifier = model_data['classifier']
    label_map = model_data.get('labels', {0: 'Negative', 1: 'Neutral', 2: 'Positive'})

    features = vectorizer.transform([text])
    prediction = classifier.predict(features)[0]
    proba = classifier.predict_proba(features)[0]
    confidence = max(proba)

    return label_map[prediction], float(confidence)


def _predict_keywords(text: str) -> tuple[str, float]:
    """Simple keyword-based fallback."""
    lower = text.lower()
    positive = ['amazing', 'awesome', 'excellent', 'fantastic', 'great', 'wonderful',
                'superb', 'brilliant', 'outstanding', 'incredible', 'loved', 'best',
                'beautiful', 'enjoyed', 'perfect', 'masterpiece', 'stunning', 'good']
    negative = ['terrible', 'awful', 'horrible', 'bad', 'worst', 'boring', 'waste',
                'disappointing', 'poor', 'dull', 'overrated', 'stupid', 'hated',
                'pathetic', 'failed', 'slow', 'confusing', 'disliked', 'rubbish']

    pos_count = sum(1 for w in positive if w in lower)
    neg_count = sum(1 for w in negative if w in lower)

    if pos_count > neg_count:
        score = min(0.99, 0.55 + pos_count * 0.08)
        return 'Positive', score
    elif neg_count > pos_count:
        score = min(0.99, 0.55 + neg_count * 0.08)
        return 'Negative', score
    return 'Neutral', 0.50


# ── Train & Save sklearn model ────────────────────────────────────────────────

def train_and_save_model():
    """
    Train a simple Naive Bayes classifier on sample data and save to disk.
    Run this once to create model/sentiment.pkl
    """
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.feature_extraction.text import TfidfVectorizer
    import pickle, os

    # Sample training data
    texts = [
        "This movie was absolutely amazing and mind-blowing",
        "I loved every minute of this fantastic film",
        "Best movie I have ever seen, outstanding performance",
        "Brilliant direction and stunning visuals",
        "A masterpiece of modern cinema, highly recommend",
        "Incredible storyline and wonderful acting",
        "This film was terrible and a waste of time",
        "Worst movie ever, completely boring and awful",
        "Horrible acting and dull storyline",
        "Disappointing and overrated, very poor quality",
        "Awful direction, I hated every moment",
        "Pathetic story and confusing plot",
        "The movie was okay, nothing special",
        "Average film with some good and bad parts",
        "Decent but not great, mixed feelings",
        "It was alright, could have been better",
        "Somewhat entertaining but forgettable",
    ]
    labels = [2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X = vectorizer.fit_transform(texts)
    clf = MultinomialNB()
    clf.fit(X, labels)

    os.makedirs('model', exist_ok=True)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump({
            'vectorizer': vectorizer,
            'classifier': clf,
            'labels': {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
        }, f)
    print("✅ Model saved to", MODEL_PATH)


if __name__ == '__main__':
    train_and_save_model()
