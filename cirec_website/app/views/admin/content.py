from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from app.views.admin import bp
from app.models.article import Article
from app.extensions import db

@bp.route('/content/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        # Handle file upload logic here
        flash('Article uploaded successfully!', 'success')
        return redirect(url_for('admin.dashboard'))
    
    return render_template('admin/content/upload.html')