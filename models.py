
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class PredictionModel(db.Model):
    __tablename__="houseprediction"
    id=db.Column(db.Integer(), primary_key=True, autoincrement=True)
    area=db.Column(db.Integer())
    bedrooms=db.Column(db.Integer())
    bathrooms=db.Column(db.Integer())
    stories=db.Column(db.Integer())
    mainroad=db.Column(db.Integer())
    parking=db.Column(db.Integer())
    prefarea=db.Column(db.Integer())
    guestroom=db.Column(db.Integer())
    basement=db.Column(db.Integer())
    hotwaterheating=db.Column(db.Integer())
    airconditioning=db.Column(db.Integer())
    furnished=db.Column(db.Integer())
    semi_furnished=db.Column(db.Integer())
    unfurnished=db.Column(db.Integer())
    price=db.Column(db.Integer())
    
    def __init__(self,area,bedrooms,bathrooms,stories,mainroad,
    parking,prefarea,guestroom,basement,hotwaterheating, 
    airconditioning,furnished,semi_furnished,unfurnished,price ):

        self.area=area
        self.bedrooms=bedrooms
        self.bathrooms=bathrooms
        self.stories=stories
        self.mainroad=mainroad
        self.parking=parking
        self.prefarea=prefarea
        self.guestroom=guestroom
        self.basement=basement
        self.hotwaterheating=hotwaterheating
        self.airconditioning=airconditioning
        self.furnished=furnished
        self.semi_furnished=semi_furnished
        self.unfurnished=unfurnished
        self.price=price

        



    
