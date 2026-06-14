/**
 * validation.js – CineAI Form Validation
 * Validates: name, email, mobile number (Indian format)
 */

// ---- Utility Validators ----
function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
}

function isValidMobile(mobile) {
  // Indian mobile: starts with 6-9, exactly 10 digits
  return /^[6-9]\d{9}$/.test(mobile.trim());
}

function isValidName(name) {
  return name.trim().length >= 2;
}

// ---- Set field validity state ----
function setFieldState(field, isValid, message = '') {
  if (isValid) {
    field.classList.remove('is-invalid');
    field.classList.add('is-valid');
  } else {
    field.classList.remove('is-valid');
    field.classList.add('is-invalid');
    const feedback = field.parentElement.querySelector('.invalid-feedback');
    if (feedback && message) feedback.textContent = message;
  }
}

// ---- Real-time validation listeners ----
function attachRealTimeValidation() {
  document.querySelectorAll('input[type="text"], input[type="email"], input[type="tel"], textarea').forEach(field => {
    field.addEventListener('input', () => {
      if (field.id && field.id.toLowerCase().includes('mobile')) {
        setFieldState(field, isValidMobile(field.value), 'Enter a valid 10-digit mobile number (starts with 6-9).');
      } else if (field.type === 'email') {
        setFieldState(field, isValidEmail(field.value), 'Enter a valid email address.');
      } else if (field.required) {
        setFieldState(field, field.value.trim().length > 0, 'This field is required.');
      }
    });
  });
}

// ---- Review Form Validation ----
document.addEventListener('DOMContentLoaded', () => {
  attachRealTimeValidation();

  const reviewForm = document.getElementById('reviewForm');
  if (reviewForm) {
    reviewForm.addEventListener('submit', function(e) {
      e.preventDefault();
      if (validateReviewForm()) {
        document.getElementById('formSuccess').classList.remove('d-none');
        setTimeout(() => {
          window.location.href = 'http://127.0.0.1:8000/blog/create/';
        }, 2000);
      }
    });
  }
});

function validateReviewForm() {
  let valid = true;

  const name = document.getElementById('reviewName');
  const email = document.getElementById('reviewEmail');
  const mobile = document.getElementById('reviewMobile');
  const movie = document.getElementById('reviewMovie');
  const text = document.getElementById('reviewText');

  // Name validation
  if (!isValidName(name.value)) {
    setFieldState(name, false, 'Name must be at least 2 characters.');
    valid = false;
  } else setFieldState(name, true);

  // Email validation
  if (!isValidEmail(email.value)) {
    setFieldState(email, false, 'Enter a valid email address (e.g. user@example.com).');
    valid = false;
  } else setFieldState(email, true);

  // Mobile validation
  if (!isValidMobile(mobile.value)) {
    setFieldState(mobile, false, 'Enter a valid 10-digit Indian mobile number (starts with 6-9).');
    valid = false;
  } else setFieldState(mobile, true);

  // Movie title validation
  if (!movie.value.trim()) {
    setFieldState(movie, false, 'Please enter the movie title.');
    valid = false;
  } else setFieldState(movie, true);

  // Review text validation
  if (text.value.trim().length < 10) {
    setFieldState(text, false, 'Review must be at least 10 characters long.');
    valid = false;
  } else setFieldState(text, true);

  return valid;
}
