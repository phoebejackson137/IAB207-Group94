from flask import Blueprint, flash, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from . import db

# Create a blueprint - make sure all BPs have unique names
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/userrego', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if the username or email already exists
        existing_user = User.query.filter((User.username == form.username.data) | 
                                          (User.emailid == form.email.data)).first()
        if existing_user is None:
            new_user = User(name=form.name.data,
                            emailid=form.email.data,
                            username=form.username.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('You have successfully registered!', 'success')
            return redirect(url_for('login'))  # Redirect to the login page after registration
        else:
            flash('Username or email already exists.', 'error')

    return render_template('userrego.html', form=form)

@auth_bp.route('/userlogin', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))  # Redirect to home if already logged in

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Logged in successfully!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))  # Redirect to next or home page
        else:
            flash('Invalid username or password.', 'error')
    return render_template('userlogin.html', form=form)

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return 'Welcome to your Dashboard!'

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('userlogin.html'))
