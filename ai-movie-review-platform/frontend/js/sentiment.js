/**
 * sentiment.js – Calls FastAPI sentiment analysis endpoint
 * Falls back to TextBlob-style client estimation if API is offline
 */

async function analyzeSentiment() {
  const input = document.getElementById('sentimentInput');
  const result = document.getElementById('sentimentResult');
  const text = input.value.trim();

  if (!text) {
    result.className = 'sentiment-result mt-3 neutral';
    result.innerHTML = '⚠️ Please enter some text to analyze.';
    result.classList.remove('d-none');
    return;
  }

  result.className = 'sentiment-result mt-3';
  result.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i> Analyzing...';
  result.classList.remove('d-none');

  try {
    const response = await fetch('http://127.0.0.1:8001/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });

    if (!response.ok) throw new Error('API error');

    const data = await response.json();
    displayResult(result, data.sentiment, data.score, text);

  } catch (err) {
    // Fallback: basic client-side keyword analysis
    const fallbackResult = clientSideSentiment(text);
    displayResult(result, fallbackResult.sentiment, fallbackResult.score, text, true);
  }
}

function displayResult(result, sentiment, score, text, isFallback = false) {
  const icons = { Positive: '😊', Negative: '😞', Neutral: '😐' };
  const cls = sentiment.toLowerCase();
  const note = isFallback ? ' <small>(FastAPI offline – using client fallback)</small>' : '';
  const scoreText = score !== undefined ? ` | Score: ${parseFloat(score).toFixed(2)}` : '';

  result.className = `sentiment-result mt-3 ${cls}`;
  result.innerHTML = `${icons[sentiment] || '🎬'} Sentiment: <strong>${sentiment}</strong>${scoreText}${note}`;
}

// Client-side fallback sentiment using keyword lists
function clientSideSentiment(text) {
  const lower = text.toLowerCase();

  const positiveWords = [
    'amazing', 'awesome', 'excellent', 'fantastic', 'great', 'wonderful', 'superb',
    'brilliant', 'outstanding', 'incredible', 'loved', 'best', 'beautiful', 'enjoyed',
    'perfect', 'masterpiece', 'stunning', 'thrilling', 'captivating', 'entertaining',
    'good', 'nice', 'recommend', 'impressive'
  ];

  const negativeWords = [
    'terrible', 'awful', 'horrible', 'bad', 'worst', 'boring', 'waste', 'disappointing',
    'poor', 'dull', 'overrated', 'ridiculous', 'stupid', 'nonsense', 'hated', 'pathetic',
    'failed', 'slow', 'confusing', 'disliked', 'rubbish', 'mediocre', 'forgettable'
  ];

  let posScore = 0, negScore = 0;
  positiveWords.forEach(w => { if (lower.includes(w)) posScore++; });
  negativeWords.forEach(w => { if (lower.includes(w)) negScore++; });

  let sentiment, score;
  if (posScore > negScore) {
    sentiment = 'Positive';
    score = Math.min(0.99, 0.5 + posScore * 0.1).toFixed(2);
  } else if (negScore > posScore) {
    sentiment = 'Negative';
    score = Math.min(0.99, 0.5 + negScore * 0.1).toFixed(2);
  } else {
    sentiment = 'Neutral';
    score = '0.50';
  }

  return { sentiment, score };
}

// Allow Enter key to trigger analysis
document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('sentimentInput');
  if (input) {
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && e.ctrlKey) analyzeSentiment();
    });
  }
});
