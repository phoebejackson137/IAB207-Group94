"""
Determines what content is in the viewport
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import SearchEventsForm, OrderForm, EventForm
from .models import Event, Order,Comment
from . import db
from flask_login import login_required, current_user
from datetime import datetime
#for file upload
from werkzeug.utils import secure_filename
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/', defaults={'active_tab': 'All'})
@main_bp.route('/<active_tab>')
def index(active_tab):
    """Landing Page"""
    form=SearchEventsForm()
    search_form=SearchEventsForm()
    active = active_tab
    events= [] 
    if active == "All": 
        events = Event.query.all()
    else:
        for event in db.session.query(Event).filter_by(tag1=active):
            events.append(event)
    return render_template('index.html',form=form, events=events, active=active,search_form=search_form)


@main_bp.route('/unauth-event-detail-view', methods=['GET', 'POST'])
def view_event():
    """Event Detail View"""
    event_id = request.args.get('target_event')
    event = db.session.scalar(db.select(Event).where(Event.id==event_id))
    comments = Comment.query.filter_by(event_id=event_id).order_by(Comment.timestamp.desc()).all()
   
    return render_template('event-detail-view.html', event=event, form=None,comments=comments)


@main_bp.route('/view-booked-events')
def see_bookings():
    """Event Creation Page"""
    events = []
    orders = []

    for order in db.session.query(Order).filter_by(user_id=1):
        print("ORDER CONFIRMATION NUM-------------" + str(order.confirmation_num))
        orders.append(order)
        event = db.session.query(Event).filter_by(id=order.event_id).first()
        events.append(event)
  
    #for order in orders:
    #    events.append(db.session.scalar(db.select(Event).where(Event.id==order.event_id)))
    #    print("events:" + str(order.confirmation_num))
    
    return render_template('user-booking-history.html',orders=orders, events=events)

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


def check_file(form):
  img_file = form.image.data
  #getting the file data from form
  filename = img_file.filename
  # get the current path of the module file… store file relative to this path
  BASE_PATH = os.path.dirname(__file__)
  #upload file location – directory of this file/static/img
  upload_path = os.path.join(BASE_PATH, 'static/img', secure_filename(filename))
  # save the file and return the db upload path
  img_file.save(upload_path)