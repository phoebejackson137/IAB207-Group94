"""
Data structures given in the assessment folder
"""
from datetime import datetime
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)#should be 128 in length to store hash
    
    usertype = db.Column(db.String(20), nullable=False, default='guest')


    def __repr__(self):
        return "<Name: {}, id: {}>".format(self.name, self.id)


class Event(db.Model):
    """Event table"""
    __tablename__='events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), index=True, unique=False, nullable=False)
    description = db.Column(db.String(250), index=True, unique=False, nullable=False)
    location = db.Column(db.String(250), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    cover_image_path = db.Column(db.String(250))
    status = db.Column(db.String(250), nullable=False,default='Open')

    orders = db.relationship('Order', backref='event')

    def __init__(self,title,description,location,start_time,cover_img_path):
        self.title = title
        self.description = description
        self.location = location
        self.start_time = start_time
        self.cover_image_path = cover_img_path

    

class Order(db.Model):
    __tablename__='orders'
    confirmation_num = db.Column(db.Integer, unique=True, primary_key = True)
    num_tickets = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Double, nullable=False)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))  
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', backref='comments')
    event = db.relationship('Event', backref='comments')


