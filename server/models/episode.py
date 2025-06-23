from . import db

class Episode(db.Model):
    """
    Episode model representing a single episode of the show.
    """
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True) 
    date = db.Column(db.Date, nullable=False) 
    number = db.Column(db.Integer, nullable=False) 

    appearances = db.relationship('Appearance', backref='episode', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        """
        Returns a string representation of the Episode object.
        """
        return f'<Episode {self.number} on {self.date}>'

