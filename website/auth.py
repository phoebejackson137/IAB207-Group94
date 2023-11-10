from flask import Blueprint, flash, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User, Comment, Event
from .forms import LoginForm, RegisterForm, CommentForm
from flask_login import login_user, login_required,logout_user, current_user
from . import db
#asdf
# Create a blueprint - make sure all BPs have unique names
bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():  
  #create the form
    form = RegisterForm()
    #this line is called when the form - POST
    if form.validate_on_submit():
      print('Register form submitted')
       
      #get username, password and email from the form
      uname =form.username.data
      pwd = form.password.data
      email=form.email.data
      utype =form.usertype.data
      
      pwd_hash = generate_password_hash(pwd)
      #create a new user model object
      new_user = User(name=uname, password_hash=pwd_hash, emailid=email, usertype=utype)
      db.session.add(new_user)
      db.session.commit()
      flash("Registered user successfully")
      return redirect(url_for('auth.register'))
       
    return render_template('forms.html', form=form, heading='Register')

@bp.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  error=None
  if(form.validate_on_submit()):
    user_name = form.username.data
    password = form.password.data
    u1 = User.query.filter_by(name=user_name).first()
    
        #if there is no user with that name
    if u1 is None:
      error='Incorrect user name'
    #check the password - notice password hash function
    elif not check_password_hash(u1.password_hash, password): # takes the hash and password
      error='Incorrect password'
    if error is None:
    #all good, set the login_user
      login_user(u1)
      return redirect(url_for('main.index'))
    else:
      print(error)
      flash(error)
    #it comes here when it is a get method
  return render_template('forms.html', form=form, heading='Login')



@bp.route('/comment', methods=['GET', 'POST'])
@login_required
def comment():
    event_id = request.args.get("event_id")
    event = db.session.scalar(db.select(Event).where(Event.id==event_id))
    print("HERE___________" + event_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(user_id=current_user.id, event_id=event_id, text=form.text.data)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted.', 'success')

        return redirect(url_for('main.view_event', target_event=event.id))  # Redirect to the event detail page
    
    return render_template('comment.html', form=form)  # Render the comment form


@bp.route('/dashboard')
@login_required
def dashboard():
    return 'Welcome to your Dashboard!'

@bp.route('/logout')
def logout():
  logout_user()
  return 'Successfully logged out user'
