from flask import Flask, render_template
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

    # Import models
    from app.models import user, article

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

    # Home route
    @app.route('/')
    def index():
        return render_template('base/base.html')

    return app