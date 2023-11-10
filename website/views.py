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



@main_bp.route('/create-event', methods=['GET', 'POST'])
@login_required
def create_event():
    form = EventForm()
    if request.method == 'POST' and form.validate_on_submit():
        filename = check_file(form)
        if filename:
            new_event = Event(
                title=form.name.data,
                tag1="Your Tag1 Field",  # Update this based on your form
                description=form.description.data,
                location=form.location.data,
                start_time=form.start_time.data,
                cover_image_path=filename,
                total_num_tickets=form.total_num_tickets.data,
                price_per_ticket=form.price_per_ticket.data,
                status=form.event_status.data,
                long_description=form.description.data
            )
            db.session.add(new_event)
            db.session.commit()
            flash('Event created successfully!', 'success')
            return redirect(url_for('some_route_name'))  # Redirect to a relevant route
        else:
            flash('There was an error with the file upload.', 'error')

    return render_template('event-update-or-create.html', form=form)


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