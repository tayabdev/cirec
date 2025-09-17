from flask import jsonify, request
from app.views.api import bp
from app.models.article import Article

@bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify({'results': []})
    
    # Simple keyword search for now
    results = Article.query.filter(
        Article.title.contains(query) | 
        Article.content.contains(query)
    ).limit(20).all()
    
    return jsonify({
        'results': [
            {
                'id': article.id,
                'title': article.title,
                'summary': article.summary or article.content[:100] + '...' if article.content else '',
                'author': article.author
            } for article in results
        ]
    })