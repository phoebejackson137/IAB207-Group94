"""
Determines what content is in the viewport
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import SearchEventsForm, OrderForm
from .models import Event, Order
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Landing Page"""
    form=SearchEventsForm()
    events= Event.query.all()
    return render_template('index.html',form=form, events=events)

@main_bp.route('/event-detail-view', methods=['GET', 'POST'])
def view_event():
    """Event Detail View"""
    form = OrderForm()
    event_id = request.args.get('target_event')
    event = db.session.scalar(db.select(Event).where(Event.id==event_id))

    if request.method == 'POST' and form.validate():
        user_id = 1
        total_price = 5.50
        order = Order(form.num_tickets.data, total_price, event_id, user_id)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('main.see_bookings'))
    elif request.method == 'POST' and not form.validate():
        for error in form.errors:
            print("error: "+error)
        flash('SYSTEM ERROR: Try again later')
    return render_template('event-detail-view.html', event=event, form=form)

@main_bp.route('/create-event')
def create_event():
    """Event Creation Page"""
    return render_template('event-update-or-create.html')

@main_bp.route('/view-booked-events')
def see_bookings():
    """Event Creation Page"""
    return render_template('user-booking-history.html')

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


