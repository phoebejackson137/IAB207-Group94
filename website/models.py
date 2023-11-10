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

    def __init__(self,name,email,password):
        self.name = name
        self.emailid = email
        self.password_hash = password

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
    total_num_tickets = db.Column(db.Integer, nullable=False)
    num_tickets_sold = db.Column(db.Integer, nullable=False, default=0)
    price_per_ticket = db.Column(db.Double, nullable=False, default=0.00)
    status = db.Column(db.String(250), nullable=False,default='Open')
    long_description = db.Column(db.String(1000),nullable=False)

    orders = db.relationship('Order', backref='event')

    def __init__(self,title,description,location,start_time, cover_img_path, total_num_tickets,
                 price_per_ticket=0.00, num_tickets_sold=0, status='Open',long_description=""):
        self.title = title
        self.description = description
        self.location = location
        self.start_time = start_time
        self.cover_image_path = cover_img_path
        self.total_num_tickets = total_num_tickets
        self.num_tickets_sold = num_tickets_sold
        self.price_per_ticket = price_per_ticket
        self.status = status
        if long_description == "":
            self.long_description = description
        else:
            self.long_description = long_description
        
        

class Order(db.Model):
    __tablename__='orders'
    confirmation_num = db.Column(db.Integer, unique=True, primary_key = True)
    num_tickets = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Double, nullable=False)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self,num_tickets,total_price,event_id,user_id):
        self.num_tickets = num_tickets
        self.total_price = total_price
        self.event_id = event_id
        self.user_id = user_id

        

class Comment(db.Model):
    """Comment Table"""
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)

# class User(db.Model, UserMixin):
#     """User data table"""
#     __tablename__='users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), index=True, unique=True, nullable=False)
#     emailid = db.Column(db.String(100), index=True, nullable=False)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password_hash = db.Column(db.String(255), nullable=False)#should be 128 in length to store hash
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#     usertype = db.Column(db.String(20), nullable=False, default='guest')
    
#     orders = db.relationship('Order', backref='user')

#     def __repr__(self):
#         return "<Name: {}, id: {}>".format(self.name, self.id)