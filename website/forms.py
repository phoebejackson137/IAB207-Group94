"""
Flask forms
"""
from flask_wtf import FlaskForm
from wtforms.fields import (
    FormField, SelectField, IntegerField, DecimalField,TextAreaField,
    SubmitField, StringField, PasswordField, DateField, FileField)
from wtforms.validators import InputRequired, Email, EqualTo, NumberRange
from flask_wtf.file import FileRequired, FileField, FileAllowed
from .user_forms import ALLOWED_FILE

class TelephoneForm(FlaskForm):
    """Directly from the Flask WTForms documentation - recommended to store phone numbers"""
    country_code = IntegerField('Country Code', validators=[InputRequired()])
    area_code    = IntegerField('Area Code/Exchange', validators=[InputRequired()])
    number       = StringField('Number')

class EventForm(FlaskForm):
    """Create new event"""
    title = StringField('Title', validators=[InputRequired()])
    tag1 = SelectField('Tag', choices=['social', 'public talk', 'workshop', 'trivia', 'competition'])
    description = TextAreaField('Description', validators = [InputRequired()])
    location = StringField('Location')
    start_time = DateField('Start time', validators=[InputRequired()])
    image = FileField('Upload file')
    num_tix = IntegerField('Number of Tickets Available')
    price_per = DecimalField('Price per ticket')
    submit = SubmitField("Post")

class OrderForm(FlaskForm):
    """Order tickets to an event"""
    num_tickets = IntegerField('Number of tickets', validators=[InputRequired(), NumberRange(min=0, message='Must enter a number greater than 0')])
    #submit = SubmitField("Submit")

class LoginForm(FlaskForm):
  username = StringField('User Name', validators=[InputRequired()])
  password = PasswordField('Password', validators=[InputRequired()])
  submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('User Name', validators=[InputRequired()])
    email = StringField('Email ID', validators=[InputRequired(),Email() ])
    #password field
    password = PasswordField('Password', validators=[InputRequired()])
  #validator to check if the user entry is equal to password
    confirm = PasswordField('Confirm Password', 
          validators=[EqualTo('password', message='Re-enter same as Password')])

    usertype = SelectField('User Type', choices=[('guest', 'Guest'),('admin', 'Administrator')])
    submit = SubmitField('Register')

class CommentForm(FlaskForm):
    """ User comments on events """
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')

class SearchEventsForm(FlaskForm):
    """ Search field """
    search_phrase = StringField('enter keywords', validators=[InputRequired()])
    submit = SubmitField('Search')