"""
Data structures given in the assessment folder
"""
from datetime import datetime
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """User data table"""
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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), index=True, unique=False, nullable=False)
    location = db.Column(db.String(250), nullable=False)

class Comment(db.Model):
    """Comment Table"""
    id = db.Column(db.Integer, primary_key=True)

class Order(db.Model):
    """Order Table"""
    id = db.Column(db.Integer, primary_key=True)