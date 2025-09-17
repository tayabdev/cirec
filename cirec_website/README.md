# CIREC Website - Flask-based Article Management System

A comprehensive Flask web application for managing and searching articles about the Russian chemical industry.

## Features

- **User Authentication & Subscription Management**
- **Semantic AI-powered Search** (using Groq/Mistral)
- **Traditional Keyword Search**
- **Admin Panel** for content management
- **PDF Upload & Processing**
- **PostgreSQL Database**
- **Responsive UI/UX**

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and configure
4. Initialize database: `python manage.py create_db`
5. Seed database: `python manage.py seed_db`
6. Run the application: `flask run`

## Project Structure

- `app/` - Main application code
- `app/models/` - Database models
- `app/views/` - Route handlers (separated by functionality)
- `app/services/` - Business logic
- `app/templates/` - HTML templates
- `app/static/` - Static files (CSS, JS, images)
- `config/` - Configuration files
- `scripts/` - Utility scripts
- `tests/` - Test files

## Key Components

- **Authentication System**: Complete user registration, login, password reset
- **Search Engine**: Dual search (keyword + semantic AI)
- **Admin Panel**: Separated from user interface
- **Content Management**: PDF upload, article management
- **Subscription System**: Ready for payment integration

## API Endpoints

- `/api/search` - Search functionality
- `/api/articles` - Article management
- `/api/user` - User operations

## Technologies

- **Backend**: Flask, SQLAlchemy, PostgreSQL
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **AI/ML**: Sentence Transformers, Groq API
- **Authentication**: Flask-Login
- **File Processing**: PyPDF2
- **Email**: Flask-Mail
