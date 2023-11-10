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
    e1=Event("QUT Astronomy Club - Monthly Stargazing Night (December)",
             "Join us for an unforgettable evening of celestial wonder at the QUT Astronomy Club's monthly Stargazing Night, taking place this December. Immerse yourself in the magic of the night sky as we explore the cosmos from the heart of the city.", 
             "QUT Gardens Point Campus, Brisbane CBD",
             datetime(2023,12,23,18,30),
             "telescope-example-img.jpeg",
             100, 
             5.50)
    e2=Event("QUT Women in Maths Society - Careers Panel",
             "Where can your Mathematics degree take you? Come along to WiM's annual career panel to meet professionals from a range of mathematical industries and gain valuable exposure to what post-university life could have in store for you.", 
             "P-Block Level 6 ('The Atrium'), QUT Gardens Point Campus, Brisbane CBD", 
             datetime(2023,11,23,13,30), 
             "career-panel.jpg",
             25)
    e3=Event("GEMS (Gender Equity in Engineering Makes Sense) - Trivia Night",
             "Are you ready to put your knowledge to the test and support a great cause at the same time? Join us for an exciting evening of fun, facts, and fellowship at our Trivia Night!", 
             "Bot Bar, QUT Gardens Point Campus, Brisbane CBD", 
             datetime(2023,10,23,18,30), 
             "trivia.jpg",
             50)
    e4=Event("Code Network Hackathon: Innovate, Collaborate, Elevate! - Opening Ceremony", 
             "Are you ready to unleash your coding prowess and creativity? Join us at the 'Code Network Hackathon: Innovate, Collaborate, Elevate!' for an exhilarating coding challenge like no other!",
             "'The Precinct', 315 Brunswick St, Fortitude Valley QLD 4006",
             datetime(2023,6,10,10,45),
             "hackathon.png",
             150,
             10.00)
    e5=Event("QUT BANDS (Business Analysis and Data Science) Club - Global Business Analysis Day!", 
             "Exciting news! Join us for a fantastic collaboration between BAPL and QUTBANDS as we celebrate Global Business Analysis Day!", 
             "Level 3 BAPL Brisbane Office, 183 North Quay, Brisbane City QLD 4000",
             datetime(2023,11,1,16),
             "global-BA-day.png",
             60,
             24.95)
    e6=Event("Q-Aero (QUT Aerospace Society) - Guest Lecturer", 
             "Interested in space? Come hear QUT Centre for Robotics Chief Investigator A/Prof Thierry Peynot's talk on 'How rovers can navigate autonomously on planetary bodies'",
             "P-514, QUT Gardens Point Campus, Brisbane CBD",
             datetime(2023,9,5,17,30),
             "space-robots.jpeg",
             120)
    e7=Event("QUT x UQ Biomedical Industry and Research Showcase", 
             "Calling all undergrads, postgrads, and enthusiasts of the emerging Biomedical industry! Join us for a phenomenal event that brings together the best in the field - the Biomedical (Multidisciplinary) Industry and Research Showcase!",
             "Global Change Institute, UQ Saint Lucia Campus, St Lucia QLD 4067",
             datetime(2023,7,21,9,30),
             "showcase.jpg",
             250,
             25.00)
    e8=Event("QUT HDR Society of Public Health and Social Work - Celebratory Dinner", 
             "Join us for an unforgettable HDR Celebration Dinner! Limited spots available, so RSVP now! Indulge in a scrumptious banquet and enjoy the evening with fellow achievers.",
             "Happy Boy, Fortitude Valley",
             datetime(2023,11,8,17,30),
             "HDR-dinner.jpeg",
             30,
             32.00)
    e9=Event("WOMEN'S NDIS INVESTING WORKSHOP: Empowerment Through SDA Investing", 
             "This event is focused on a deep dive into NDIS property investing, if you're new to the concept or a seasoned investor, this event is designed to inform, inspire, and to leave you with no doubt about this program that is changing financial futures of property investors all over Australia.",
             "Online",
             datetime(2024,2,4,10),
             "woman-speech.jpg",
             1000)
    e10=Event("Brisbane Business Hub - Turn Your Dreams into Reality with Neuroscience", 
              "Join this interactive workshop and learn how the brain science of success can help you to turn your dreams into reality in your career, or business, or other area of life",
              "Level 2, 155 Queen Street, Brisbane City, QLD 4000",
              datetime(2023,4,9,11,15),
              "public-lecture-example.jpg",
              175,
              17.00)
    e11=Event("Clinical Informatics Symposium - Building the genomics revolution in health", 
              "Following the ABACBS conference, this symposium brings together leaders in the field who have dedicated their careers to bridging the gap between research and tangible health outcomes.",
              "UQ St Lucia Campus Brisbane, QLD 4072",
              datetime(2023,12,7,9),
              "uq-lecture.jpg",
              300,
              12.50)
    e12=Event("Swiss DolorClast Academy - The Latest Advances in the Treatment of Osteoarthritis", 
              "Enjoy drinks and dinner as Gavin Corica provides a scientifically proven model for the management of osteoarthritis.", 
              "The Sebel Brisbane, Cnr Albert and Charlotte St Brisbane City, QLD 4000",
              datetime(2023,12,6,19,30),
              "arthritis.jpg",
              75,
              22.50)
    
    db.session.add(e1)
    db.session.add(e2)
    db.session.add(e3)
    db.session.add(e4)
    db.session.add(e5)
    db.session.add(e6)
    db.session.add(e7)
    db.session.add(e8)
    db.session.add(e9)
    db.session.add(e10)
    db.session.add(e11)
    db.session.add(e12)
    
    db.session.commit()
    app.run()
