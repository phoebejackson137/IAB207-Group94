from website import db, create_app
from datetime import datetime
app = create_app()
ctx = app.app_context()
ctx.push()
db.drop_all()
db.create_all()

from website.models import User, Event, Order
e1=Event("Example Event","Description:blach blah blah", "Brisbane", datetime(2023,11,23,18,30), "telescope-example-img.jpeg")
db.session.add(e1)
db.session.commit()