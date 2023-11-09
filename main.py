"""
MAIN
"""
from website import db, create_app
from datetime import datetime
from website.models import User, Event, Order


if __name__ == '__main__':
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.drop_all()
    db.create_all()
    e1=Event("QUT Astronomy Club - Monthly Stargazing Night (December)","Join us for an unforgettable evening of celestial wonder at the QUT Astronomy Club's monthly Stargazing Night, taking place this December. Immerse yourself in the magic of the night sky as we explore the cosmos from the heart of the city.", "QUT Gardens Point Campus, Brisbane CBD", datetime(2023,12,23,18,30), "telescope-example-img.jpeg")
    e2=Event("Example Event 2","Description:blach blah blah", "Brisbane", datetime(2023,11,23,18,30), "telescope-example-img.jpeg")
    
    db.session.add(e1)
    db.session.add(e2)
    
    db.session.commit()
    app.run()
