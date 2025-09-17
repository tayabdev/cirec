from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.views.user import bp
from app.models.article import Article
from app.extensions import db
from datetime import datetime

@bp.route('/dashboard')
@login_required
def dashboard():
    recent_articles = Article.query.filter_by(is_published=True).limit(10).all()
    return render_template('user/dashboard/index.html', articles=recent_articles)

@bp.route('/profile')
@login_required
def profile():
    return render_template('user/profile/profile.html')

@bp.route('/subscription')
@login_required  
def subscription():
    # Add current date for template usage
    current_date = datetime.utcnow()
    return render_template('user/subscription/manage.html', current_date=current_date)

@bp.route('/articles')
@login_required
def articles():
    articles = Article.query.filter_by(is_published=True).all()
    return render_template('user/articles/list.html', articles=articles)

@bp.route('/article/<int:id>')
@login_required
def view_article(id):
    article = Article.query.get_or_404(id)
    article.view_count += 1
    db.session.commit()
    return render_template('user/articles/view.html', article=article)

@bp.route('/subscription/upgrade', methods=['POST'])
@login_required
def upgrade_subscription():
    """Handle subscription upgrade"""
    plan_type = request.form.get('plan_type')
    payment_method = request.form.get('payment_method')
    
    # TODO: Implement actual payment processing
    # For now, just activate subscription
    current_user.subscription_status = 'active'
    current_user.subscription_start = datetime.utcnow()
    
    # Set end date based on plan
    if plan_type == 'basic':
        current_user.subscription_end = datetime.utcnow().replace(month=datetime.utcnow().month + 3)
    else:
        current_user.subscription_end = datetime.utcnow().replace(year=datetime.utcnow().year + 1)
    
    db.session.commit()
    flash('Subscription upgraded successfully!', 'success')
    return redirect(url_for('user.subscription'))