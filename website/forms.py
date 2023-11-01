"""
Flask forms
"""
from flask_wtf import FlaskForm
from wtforms.fields import (
    FormField, SelectField, IntegerField, DecimalField,TextAreaField,
    SubmitField, StringField, PasswordField, DateTimeField, FileField)
from wtforms.validators import InputRequired, Email, EqualTo

class TelephoneForm(FlaskForm):
    """Directly from the Flask WTForms documentation - recommended to store phone numbers"""
    country_code = IntegerField('Country Code', validators=[InputRequired()])
    area_code    = IntegerField('Area Code/Exchange', validators=[InputRequired()])
    number       = StringField('Number')

class EventForm(FlaskForm):
    """Create new event"""
    name = StringField('Country', validators=[InputRequired()])
    description = TextAreaField('Description', validators = [InputRequired()])
    image = FileField('Cover Image', validators=[InputRequired()])
    start_time = DateTimeField('Start time', validators=[InputRequired()])
    end_time = DateTimeField('End time', validators=[InputRequired()])
    event_status = SelectField('Status', choices=['Open', 'Inactive', 'Sold Out', 'Cancelled'])
    submit = SubmitField("Create")

class OrderForm(FlaskForm):
    """Order tickets to an event"""
    num_tickets = IntegerField('Number of tickets', validators=[InputRequired()])
    price_per_ticket = DecimalField('Price per ticket')

class LoginForm(FlaskForm):
    """Login for existing users"""
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    """User registration"""
    user_name=StringField("User Name", validators=[InputRequired()])
    user_email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    mobile_number = FormField(TelephoneForm)
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

class CommentForm(FlaskForm):
    """ User comments on events """
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')

class SearchEventsForm(FlaskForm):
    """ Search field """
    search_phrase = StringField('enter keywords', validators=[InputRequired()])
    location = StringField('enter location', validators=[InputRequired()])
