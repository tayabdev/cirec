from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.views.admin import bp
from app.models.user import User
from app.models.article import Article

def admin_required(f):
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin access required')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    total_users = User.query.count()
    total_articles = Article.query.count()
    recent_users = User.query.order_by(User.created_at.desc()).limit(5).all()
    return render_template('admin/dashboard/index.html', 
                         total_users=total_users, 
                         total_articles=total_articles,
                         recent_users=recent_users)

@bp.route('/users')
@login_required
@admin_required
def users():
    users = User.query.all()
    return render_template('admin/users/list.html', users=users)

@bp.route('/articles')
@login_required
@admin_required
def articles():
    articles = Article.query.all()
    return render_template('admin/content/list.html', articles=articles)