"""
Determines what content is in the viewport
"""
from flask import Blueprint, render_template
from .forms import SearchEventsForm

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Landing Page"""
    form=SearchEventsForm()
    return render_template('index.html',form=form)

@main_bp.route('/create-event')
def create_event():
    """Event Creation Page"""
    return render_template('event-update-or-create.html')
