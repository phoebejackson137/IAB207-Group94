"""
Determines what content is in the viewport
"""
from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Landing Page"""
    return '<h1>Starter code for the assessment<h1>'
