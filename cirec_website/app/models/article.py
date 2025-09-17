from datetime import datetime
from app.extensions import db

class Article(db.Model):
    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=True)
    summary = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(100), nullable=True)
    source_file = db.Column(db.String(255), nullable=True)  # PDF filename
    file_path = db.Column(db.String(500), nullable=True)    # Full file path
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=True)
    view_count = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Article {self.title}>'
