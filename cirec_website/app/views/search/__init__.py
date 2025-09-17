from flask import Blueprint

bp = Blueprint('search', __name__)

from app.views.search import routes