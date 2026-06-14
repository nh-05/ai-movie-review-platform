"""
FastAPI App – CineAI Sentiment Analysis
Endpoint: POST /analyze
Returns sentiment: Positive / Negative / Neutral
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentiment_model import predict_sentiment

app = FastAPI(
    title="CineAI Sentiment API",
    description="AI-powered sentiment analysis for movie reviews",
    version="1.0.0"
)

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ReviewRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    score: float
    label: str


@app.get("/")
def root():
    return {
        "service": "CineAI Sentiment API",
        "version": "1.0.0",
        "endpoints": {
            "POST /analyze": "Analyze sentiment of a movie review",
            "GET /docs":     "Interactive API documentation"
        }
    }


@app.post("/analyze", response_model=SentimentResponse)
def analyze(request: ReviewRequest):
    """
    Analyze the sentiment of a movie review text.
    Returns: Positive, Negative, or Neutral with confidence score.
    """
    sentiment, score = predict_sentiment(request.text)
    label_map = {
        "Positive": "😊 Great review!",
        "Negative": "😞 Critical review",
        "Neutral":  "😐 Mixed feelings"
    }
    return SentimentResponse(
        text=request.text,
        sentiment=sentiment,
        score=round(score, 4),
        label=label_map.get(sentiment, "")
    )


@app.get("/health")
def health():
    return {"status": "ok"}
