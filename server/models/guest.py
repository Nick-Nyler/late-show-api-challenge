from models import db

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    occupation = db.Column(db.String(128), nullable=False)
    appearances = db.relationship('Appearance', backref='guest', lazy=True)