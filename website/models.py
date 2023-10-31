"""
Data structures given in the assessment folder
"""
from datetime import datetime
from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    ""

class Event(db.Model):
    ""

class Comment(db.Model):
    ""

class Order(db.Model):
    ""