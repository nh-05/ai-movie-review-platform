"""
Flask App – CineAI
Routes: /, /about, /contact
REST API: /api/movies
"""

from flask import Flask, render_template, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend


# ── HTML Routes ──────────────────────────────────────────────────────────────

@app.route('/')
def home():
    movies = load_movies()
    return render_template('home.html', movies=movies)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


# ── REST API ─────────────────────────────────────────────────────────────────

@app.route('/api/movies', methods=['GET'])
def get_movies():
    """Return full movie dataset as JSON."""
    movies = load_movies()
    return jsonify(movies)


@app.route('/api/movies/<string:title>', methods=['GET'])
def get_movie(title):
    """Return a single movie by title (case-insensitive)."""
    movies = load_movies()
    movie = next((m for m in movies if m['movie'].lower() == title.lower()), None)
    if movie:
        return jsonify(movie)
    return jsonify({'error': 'Movie not found'}), 404


# ── Helper ────────────────────────────────────────────────────────────────────

def load_movies():
    json_path = os.path.join(os.path.dirname(__file__), 'movies.json')
    with open(json_path, 'r') as f:
        return json.load(f)


# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    app.run(debug=True, port=5000)
