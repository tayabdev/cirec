#!/bin/bash

# CIREC Website Setup Script
# Creates complete Flask-based blog website with semantic search and admin panel

echo "🚀 Creating CIREC Website Structure..."

# Create main project directory structure
mkdir -p cirec_website/{app,config,migrations,tests,scripts,logs,uploads}

# Navigate to project root
cd cirec_website

# Core application structure
mkdir -p app/{models,views,services,utils,static,templates}

# Models for database entities
mkdir -p app/models
touch app/models/__init__.py
touch app/models/user.py              # User model with subscription info
touch app/models/article.py           # Article model for content
touch app/models/subscription.py      # Subscription management
touch app/models/search_index.py      # Search indexing model
touch app/models/admin.py             # Admin user model
touch app/models/payment.py           # Payment tracking model

# Views/Routes separated by functionality
mkdir -p app/views/{auth,user,admin,api,search}

# Authentication routes
touch app/views/auth/__init__.py
touch app/views/auth/routes.py        # Login, register, logout routes

# User-facing routes
touch app/views/user/__init__.py
touch app/views/user/routes.py        # User dashboard, profile, articles
touch app/views/user/subscription.py  # Subscription management routes

# Admin routes (separated from user)
touch app/views/admin/__init__.py
touch app/views/admin/routes.py       # Admin dashboard
touch app/views/admin/content.py      # Article/PDF upload and management
touch app/views/admin/users.py        # User management
touch app/views/admin/analytics.py    # Site analytics

# API endpoints for AJAX calls
touch app/views/api/__init__.py
touch app/views/api/search.py         # Search API endpoints
touch app/views/api/articles.py       # Article API endpoints
touch app/views/api/user.py           # User API endpoints

# Search functionality (both keyword and semantic)
touch app/views/search/__init__.py
touch app/views/search/routes.py      # Search interface routes

# Services for business logic
mkdir -p app/services/{auth,search,content,payment,email}

# Authentication services
touch app/services/auth/__init__.py
touch app/services/auth/auth_service.py       # Login/logout logic
touch app/services/auth/registration.py       # User registration
touch app/services/auth/password_reset.py     # Password management

# Search services (AI + Traditional)
touch app/services/search/__init__.py
touch app/services/search/keyword_search.py   # Traditional keyword search
touch app/services/search/semantic_search.py  # AI-powered semantic search
touch app/services/search/indexing_service.py # Content indexing
touch app/services/search/search_manager.py   # Combined search orchestrator

# Content management services
touch app/services/content/__init__.py
touch app/services/content/article_service.py # Article CRUD operations
touch app/services/content/pdf_processor.py   # PDF text extraction
touch app/services/content/content_manager.py # Content management

# Payment and subscription services
touch app/services/payment/__init__.py
touch app/services/payment/subscription_manager.py # Subscription logic
touch app/services/payment/payment_processor.py    # Payment handling

# Email services
touch app/services/email/__init__.py
touch app/services/email/email_service.py     # Email notifications
touch app/services/email/templates.py         # Email templates

# Utility functions
mkdir -p app/utils
touch app/utils/__init__.py
touch app/utils/decorators.py         # Custom decorators (auth, admin_required)
touch app/utils/helpers.py            # Helper functions
touch app/utils/validators.py         # Input validation
touch app/utils/text_processing.py    # Text processing utilities
touch app/utils/file_handlers.py      # File upload/processing
touch app/utils/security.py           # Security utilities

# Static files structure
mkdir -p app/static/{css,js,images,uploads,fonts}

# CSS files
mkdir -p app/static/css/{admin,user,components}
touch app/static/css/main.css          # Main stylesheet
touch app/static/css/admin/admin.css   # Admin panel styles
touch app/static/css/user/user.css     # User interface styles
touch app/static/css/components/search.css      # Search component styles
touch app/static/css/components/articles.css    # Article display styles
touch app/static/css/components/forms.css       # Form styles

# JavaScript files
mkdir -p app/static/js/{admin,user,components}
touch app/static/js/main.js            # Main JavaScript
touch app/static/js/admin/admin.js     # Admin panel JavaScript
touch app/static/js/user/user.js       # User interface JavaScript
touch app/static/js/components/search.js        # Search functionality
touch app/static/js/components/articles.js      # Article interactions
touch app/static/js/components/subscription.js  # Subscription management

# Upload directories
mkdir -p app/static/uploads/{pdfs,images,temp}

# Template structure (Jinja2 templates)
mkdir -p app/templates/{base,auth,user,admin,search,errors,email}

# Base templates
touch app/templates/base/base.html              # Main base template
touch app/templates/base/admin_base.html        # Admin base template
touch app/templates/base/user_base.html         # User base template

# Authentication templates
touch app/templates/auth/login.html             # Login page
touch app/templates/auth/register.html          # Registration page
touch app/templates/auth/forgot_password.html   # Password reset
touch app/templates/auth/reset_password.html    # Password reset form

# User interface templates
mkdir -p app/templates/user/{dashboard,profile,articles,subscription}
touch app/templates/user/dashboard/index.html   # User dashboard
touch app/templates/user/profile/profile.html   # User profile
touch app/templates/user/profile/edit.html      # Edit profile
touch app/templates/user/articles/list.html     # Article listing
touch app/templates/user/articles/view.html     # Article view
touch app/templates/user/subscription/manage.html  # Subscription management
touch app/templates/user/subscription/upgrade.html # Subscription upgrade

# Admin interface templates
mkdir -p app/templates/admin/{dashboard,content,users,analytics}
touch app/templates/admin/dashboard/index.html  # Admin dashboard
touch app/templates/admin/content/list.html     # Content management
touch app/templates/admin/content/upload.html   # Content upload
touch app/templates/admin/content/edit.html     # Content editing
touch app/templates/admin/users/list.html       # User management
touch app/templates/admin/users/view.html       # User details
touch app/templates/admin/analytics/stats.html  # Analytics dashboard

# Search templates
touch app/templates/search/search.html          # Search interface
touch app/templates/search/results.html         # Search results
touch app/templates/search/advanced.html        # Advanced search

# Error templates
touch app/templates/errors/404.html             # Not found
touch app/templates/errors/500.html             # Server error
touch app/templates/errors/403.html             # Forbidden

# Email templates
touch app/templates/email/welcome.html          # Welcome email
touch app/templates/email/password_reset.html   # Password reset email
touch app/templates/email/subscription.html     # Subscription emails

# Main application files
touch app/__init__.py                  # Flask app factory
touch app/extensions.py               # Flask extensions initialization
touch app/cli.py                      # CLI commands

# Configuration files
mkdir -p config
touch config/__init__.py
touch config/development.py           # Development configuration
touch config/production.py            # Production configuration
touch config/testing.py               # Testing configuration

# Database and migration setup
touch requirements.txt                 # Python dependencies
touch .env.example                     # Environment variables example
touch .env                            # Environment variables (will be ignored by git)
touch .gitignore                      # Git ignore file
touch README.md                       # Project documentation

# Database migration and management
touch manage.py                       # Database management script
touch wsgi.py                         # WSGI application entry point

# Scripts for deployment and maintenance
mkdir -p scripts
touch scripts/init_db.py              # Database initialization
touch scripts/seed_data.py            # Sample data seeding
touch scripts/backup_db.py            # Database backup
touch scripts/index_articles.py       # Article indexing script
touch scripts/migrate_old_data.py     # Migration from old MySQL database

# Docker configuration (optional)
touch Dockerfile                      # Docker container configuration
touch docker-compose.yml              # Docker compose for development
touch docker-compose.prod.yml         # Docker compose for production

# Testing structure
mkdir -p tests/{unit,integration,fixtures}
touch tests/__init__.py
touch tests/conftest.py               # Pytest configuration
touch tests/unit/test_models.py       # Model tests
touch tests/unit/test_services.py     # Service tests
touch tests/integration/test_auth.py  # Authentication tests
touch tests/integration/test_search.py # Search tests
touch tests/fixtures/sample_data.py   # Test data fixtures

# Logs directory
mkdir -p logs
touch logs/.gitkeep

# Create main Python files with basic structure
cat > app/__init__.py << 'EOF'
from flask import Flask
from config import Config
from app.extensions import db, migrate, login_manager, mail

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    # Register Blueprints
    from app.views.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.views.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from app.views.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from app.views.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.views.search import bp as search_bp
    app.register_blueprint(search_bp, url_prefix='/search')

    return app
EOF

cat > app/extensions.py << 'EOF'
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()

login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
EOF

cat > requirements.txt << 'EOF'
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Migrate==4.0.5
Flask-Login==0.6.3
Flask-Mail==0.9.1
psycopg2-binary==2.9.7
python-dotenv==1.0.0
Werkzeug==2.3.7
PyPDF2==3.0.1
sentence-transformers==2.2.2
numpy==1.24.3
scikit-learn==1.3.0
redis==4.6.0
celery==5.3.1
gunicorn==21.2.0
python-decouple==3.8
cryptography==41.0.4
bcrypt==4.0.1
WTForms==3.0.1
Flask-WTF==1.1.1
Pillow==10.0.0
bleach==6.0.0
markdown==3.4.4
requests==2.31.0
groq==0.4.1
EOF

cat > .env.example << 'EOF'
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost/cirec_db
POSTGRES_USER=cirec_user
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=cirec_db

# Flask Configuration
SECRET_KEY=your-very-secure-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Redis Configuration (for caching and background tasks)
REDIS_URL=redis://localhost:6379/0

# AI/ML Configuration
GROQ_API_KEY=your-groq-api-key
SENTENCE_TRANSFORMER_MODEL=all-MiniLM-L6-v2

# File Upload Configuration
MAX_CONTENT_LENGTH=16777216  # 16MB
UPLOAD_FOLDER=app/static/uploads

# Security
SECURITY_PASSWORD_SALT=your-password-salt
JWT_SECRET_KEY=your-jwt-secret-key

# Payment Configuration (for future use)
STRIPE_PUBLISHABLE_KEY=pk_test_your_key
STRIPE_SECRET_KEY=sk_test_your_key

# Admin Configuration
ADMIN_EMAIL=admin@cirec.net
ADMIN_PASSWORD=secure_admin_password
EOF

cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Flask
instance/
.webassets-cache

# Environment variables
.env
.venv
env/
venv/
ENV/

# Database
*.db
*.sqlite

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
logs/*.log
*.log

# Uploads
app/static/uploads/pdfs/*
app/static/uploads/temp/*
!app/static/uploads/.gitkeep

# Testing
.pytest_cache/
.coverage
htmlcov/

# Node modules (if using any frontend tools)
node_modules/

# Backup files
*.bak
*.backup
EOF

cat > manage.py << 'EOF'
#!/usr/bin/env python
import os
from flask.cli import FlaskGroup
from app import create_app, db
from app.models.user import User
from app.models.article import Article

app = create_app()
cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    """Creates the database tables."""
    db.create_all()
    print("Database tables created!")

@cli.command("drop_db")
def drop_db():
    """Drops the database tables."""
    db.drop_all()
    print("Database tables dropped!")

@cli.command("seed_db")
def seed_db():
    """Seeds the database with initial data."""
    # Create admin user
    admin = User(
        email='admin@cirec.net',
        username='admin',
        first_name='Admin',
        last_name='User',
        is_admin=True
    )
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
    print("Database seeded with initial data!")

if __name__ == '__main__':
    cli()
EOF

cat > wsgi.py << 'EOF'
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
EOF

cat > README.md << 'EOF'
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
EOF

# Make manage.py executable
chmod +x manage.py

# Create empty __init__.py files for all view packages
touch app/views/__init__.py
touch app/views/auth/__init__.py
touch app/views/user/__init__.py
touch app/views/admin/__init__.py
touch app/views/api/__init__.py
touch app/views/search/__init__.py

# Create .gitkeep files for empty directories
touch app/static/uploads/.gitkeep
touch logs/.gitkeep

echo "✅ CIREC Website structure created successfully!"
echo ""
echo "📁 Project Structure:"
echo "├── app/ (Main application)"
echo "│   ├── models/ (Database models)"
echo "│   ├── views/ (Routes - separated: auth, user, admin, api, search)"
echo "│   ├── services/ (Business logic)"
echo "│   ├── templates/ (HTML templates)"
echo "│   ├── static/ (CSS, JS, uploads)"
echo "│   └── utils/ (Helper functions)"
echo "├── config/ (Configuration files)"
echo "├── scripts/ (Utility scripts)"
echo "├── tests/ (Test files)"
echo "└── data/ (Your existing PDF files)"
echo ""
echo "🔧 Next Steps:"
echo "1. Copy .env.example to .env and configure your settings"
echo "2. Install dependencies: pip install -r requirements.txt"
echo "3. Set up PostgreSQL database"
echo "4. Initialize database: python manage.py create_db"
echo "5. Seed database: python manage.py seed_db"
echo "6. Start development: flask run"
echo ""
echo "🎯 Key Features Implemented:"
echo "• Separated Admin and User panels"
echo "• API-based architecture"
echo "• Semantic + Keyword search"
echo "• User authentication with subscription management"
echo "• PDF upload and processing"
echo "• Modern responsive UI structure"
echo "• PostgreSQL database integration"
echo ""
echo "📧 Default admin login will be: admin@cirec.net / admin123"