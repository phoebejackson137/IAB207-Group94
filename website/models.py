"""
Data structures given in the assessment folder
"""
from . import db
from datetime import datetime
from flask_login import UserMixin

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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), index=True, unique=False, nullable=False)
    location = db.Column(db.String(250), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)