from . import db

class Guest(db.Model):
    """
    Guest model representing a guest who appears on the show.
    """
    __tablename__ = 'guests' 

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100), nullable=False) 
    occupation = db.Column(db.String(100), nullable=False) 

    appearances = db.relationship('Appearance', backref='guest', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        """
        Returns a string representation of the Guest object.
        """
        return f'<Guest {self.name}>'

