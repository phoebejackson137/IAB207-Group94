"""
Determines what content is in the viewport
"""
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Landing Page"""
    return render_template('index.html')

@main_bp.route('/create-event')
def create_event():
    """Event Creation Page"""
    return render_template('event-update-or-create.html')
