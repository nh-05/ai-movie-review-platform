# ai-movie-review-platform


CineAI is a full-stack AI-powered Disney movie review platform where users can browse trending movies, watch trailers, analyze review sentiment using AI, and post reviews on a community blog with full authentication. Built as a multi-backend web application demonstrating the integration of three Python frameworks with a responsive frontend.

---

## Tech Stack

Frontend — HTML5, CSS3, Bootstrap 5, JavaScript

Backend — Flask, FastAPI, Django, Django REST Framework

AI/ML — TextBlob, scikit-learn, Naive Bayes Classifier, TF-IDF Vectorization

Database — SQLite

---

## Features

Responsive movie browsing website with carousel, Disney movie poster cards and embedded YouTube trailers

AI sentiment analysis that classifies user reviews as Positive, Negative or Neutral in real time

Community blog with full Create, Read, Update and Delete functionality

User registration, login and logout with session-based authentication

REST APIs served by both Flask and Django REST Framework

Client-side form validation for name, email and mobile number with real-time feedback

Fallback keyword-based sentiment analysis if FastAPI server is offline

---

## Project Structure

frontend — Responsive HTML, CSS and JavaScript website with four pages

flask_app — Flask application serving movie data as a REST API with three HTML routes

fastapi_app — FastAPI service running AI sentiment analysis on review text

django_blog — Django blog system with authentication, CRUD, templates and DRF API

---

## API Endpoints

Flask — GET /api/movies returns all movies, GET /api/movies/title returns a single movie

FastAPI — POST /analyze accepts review text and returns sentiment and confidence score

Django — GET /api/posts/ returns all blog posts, POST /api/posts/ creates a new post

