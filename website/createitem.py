from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitedata.sqlite'
db = SQLAlchemy(app)

# Create a database model for events
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    date = db.Column(db.String(50))
    status = db.Column(db.String(20))  # Open, Inactive, Sold Out, or Cancelled
    owner = db.Column(db.String(100))

# Route for creating an event
@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        date = request.form['date']
        status = request.form['status']
        owner = request.form['owner']

        # Create a new event and add it to the database
        new_event = Event(name=name, description=description, date=date, status=status, owner=owner)
        db.session.add(new_event)
        db.session.commit()

        return redirect(url_for('view_events'))

    return render_template('create_event.html')

# Route for viewing events
@app.route('/view_events')
def view_events():
    events = Event.query.all()
    return render_template('view_events.html', events=events)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
