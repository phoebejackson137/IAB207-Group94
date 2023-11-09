"""
Determines what content is in the viewport
"""
from flask import Blueprint, render_template, request, redirect, url_for
from .forms import SearchEventsForm
from .models import Event
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Landing Page"""
    form=SearchEventsForm()
    events= Event.query.all()
    return render_template('index.html',form=form, events=events)

@main_bp.route('/event-detail-view')
def view_event():
    """Event Detail View"""
    event_id = request.args.get('target_event')
    event = db.session.scalar(db.select(Event).where(Event.id==event_id))
    return render_template('event-detail-view.html', event=event)

@main_bp.route('/create-event')
def create_event():
    """Event Creation Page"""
    return render_template('event-update-or-create.html')

@main_bp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        destinations = db.session.scalars(db.select(Event)).where(Event.description.like(query))
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))
    
eventbp = Blueprint('event', __name__, url_prefix='/event')

@eventbp.route('/<id>')
def show(id):
    event = db.session.scalar(db.select(Event).where(Event.id==id))
    return render_template('event-detail-view.html', event=event)
