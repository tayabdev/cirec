from flask import render_template, request, redirect, url_for, jsonify, abort
from flask_login import login_required, current_user
from app.views.search import bp
from app.models.article import Article
from app.extensions import db
from sqlalchemy import or_, and_
from datetime import datetime, timedelta

@bp.route('/')
def search():
    query = request.args.get('q', '')
    results = []
    
    if query:
        # Get filter parameters
        date_range = request.args.get('date_range')
        category = request.args.get('category')
        company = request.args.get('company')
        product = request.args.get('product')
        region = request.args.get('region')
        doc_type = request.args.get('doc_type')
        
        # Build base query
        search_query = Article.query.filter_by(is_published=True)
        
        # Apply text search
        if query:
            search_conditions = or_(
                Article.title.contains(query),
                Article.content.contains(query),
                Article.summary.contains(query)
            )
            search_query = search_query.filter(search_conditions)
        
        # Apply filters
        if date_range:
            date_filters = {
                '1_month': datetime.utcnow() - timedelta(days=30),
                '3_months': datetime.utcnow() - timedelta(days=90),
                '6_months': datetime.utcnow() - timedelta(days=180),
                '1_year': datetime.utcnow() - timedelta(days=365)
            }
            if date_range in date_filters:
                search_query = search_query.filter(
                    Article.created_at >= date_filters[date_range]
                )
        
        if company:
            search_query = search_query.filter(
                or_(
                    Article.title.contains(company),
                    Article.content.contains(company)
                )
            )
        
        if product:
            search_query = search_query.filter(
                or_(
                    Article.title.contains(product),
                    Article.content.contains(product)
                )
            )
        
        # Execute search
        results = search_query.order_by(Article.created_at.desc()).limit(50).all()
    
    return render_template('search/search.html', query=query, results=results)

@bp.route('/preview/<int:id>')
def preview_article(id):
    """Show article preview - available to all users"""
    article = Article.query.get_or_404(id)
    
    # Create preview version with limited content
    preview_data = {
        'id': article.id,
        'title': article.title,
        'author': article.author,
        'created_at': article.created_at,
        'summary': article.summary[:200] + '...' if article.summary else None,
        'content': article.content[:300] + '...' if article.content else None,
        'is_preview': True
    }
    
    return render_template('search/article_preview.html', article=preview_data)

@bp.route('/suggestions')
def search_suggestions():
    """API endpoint for search suggestions"""
    query = request.args.get('q', '').lower()
    
    if len(query) < 2:
        return jsonify([])
    
    # Get suggestions from article titles
    suggestions = Article.query.filter(
        Article.title.ilike(f'%{query}%')
    ).limit(10).all()
    
    results = []
    for article in suggestions:
        # Extract relevant parts of the title
        title = article.title.lower()
        if query in title:
            results.append(article.title)
    
    # Add some predefined suggestions
    predefined = [
        'Russian petrochemical industry',
        'Gazprom chemical production',
        'Sibur polymer market',
        'LUKOIL refinery capacity',
        'Russian fertilizer exports',
        'Chemical industry Moscow',
        'Ethylene production Russia',
        'Polymer market analysis'
    ]
    
    # Filter predefined suggestions
    for suggestion in predefined:
        if query in suggestion.lower() and suggestion not in results:
            results.append(suggestion)
    
    return jsonify(results[:8])  # Return max 8 suggestions