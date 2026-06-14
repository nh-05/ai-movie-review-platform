# 🎬 CineAI – AI Movie Review & Blog Platform

A full-stack AI-powered movie review platform combining HTML/Bootstrap frontend, Flask REST API, FastAPI ML service, and a Django blog system with authentication and CRUD.

---

## 📁 Project Structure

```
ai-movie-review-platform/
├── frontend/               ← HTML5 + Bootstrap website
├── flask_app/              ← Flask REST API + routes
├── fastapi_app/            ← FastAPI sentiment analysis
├── django_blog/            ← Django blog + DRF API
├── requirements.txt        ← All Python dependencies
└── README.md
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
python -m textblob.download_corpora  # Download TextBlob data
```

---

### 2. Run Flask App (Port 5000)

```bash
cd flask_app
python app.py
```

Open: http://127.0.0.1:5000  
API:  http://127.0.0.1:5000/api/movies

---

### 3. Run FastAPI Sentiment API (Port 8001)

```bash
cd fastapi_app

# Optional: pre-train sklearn model (or just use TextBlob)
python sentiment_model.py

# Start the server
uvicorn main:app --reload --port 8001
```

Open: http://127.0.0.1:8001/docs (interactive API docs)

**Example request:**
```json
POST http://127.0.0.1:8001/analyze
{ "text": "This movie was absolutely amazing!" }
```

**Response:**
```json
{ "sentiment": "Positive", "score": 0.85, "label": "😊 Great review!" }
```

---

### 4. Run Django Blog (Port 8000)

```bash
cd django_blog

# First-time setup
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```

Open: http://127.0.0.1:8000

**Endpoints:**
| URL | Description |
|-----|-------------|
| `/` | Homepage |
| `/blog/` | All reviews |
| `/blog/create/` | Create review (login required) |
| `/blog/<id>/` | Review detail |
| `/blog/<id>/edit/` | Edit review |
| `/blog/<id>/delete/` | Delete review |
| `/login/` | Login |
| `/register/` | Register |
| `/api/posts/` | DRF REST API |
| `/admin/` | Django admin |

---

### 5. Open Frontend

Open `frontend/index.html` in your browser (or serve with Live Server).

Make sure all backends are running on their respective ports for full functionality.

---

## ✨ Features

| Feature | Technology |
|---------|-----------|
| Responsive design | Bootstrap 5 |
| Movie banners + carousel | HTML5 + Bootstrap |
| Form validation (name, email, mobile) | Vanilla JavaScript |
| Flask routes (/, /about, /contact) | Flask 3 |
| Movie dataset REST API | Flask + JSON |
| AI sentiment analysis | FastAPI + TextBlob/sklearn |
| Blog CRUD | Django 5 |
| User authentication | Django Auth |
| REST API for blog | Django REST Framework |

---

## 🔗 API Reference

### Flask API
- `GET /api/movies` → All movies
- `GET /api/movies/<title>` → Single movie

### FastAPI Sentiment API
- `POST /analyze` → `{ "text": "..." }` → `{ "sentiment": "Positive", "score": 0.9 }`
- `GET /docs` → Swagger UI

### Django DRF API
- `GET  /api/posts/` → All blog posts
- `POST /api/posts/` → Create post (auth required)
- `GET  /api/posts/<id>/` → Single post
- `PUT  /api/posts/<id>/` → Update post (auth required)
- `DELETE /api/posts/<id>/` → Delete post (auth required)

---

## 🧪 Run Django Tests

```bash
cd django_blog
python manage.py test blog
```

---

## 📦 Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend 1**: Python Flask 3 + Flask-CORS
- **Backend 2**: FastAPI + Uvicorn + TextBlob / scikit-learn
- **Backend 3**: Django 5 + Django REST Framework
- **Database**: SQLite (Django)
- **ML**: TextBlob sentiment analysis / Naive Bayes classifier
