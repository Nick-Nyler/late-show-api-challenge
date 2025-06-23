from . import db

class Appearance(db.Model):
    """
    Appearance model representing a guest's appearance in a specific episode.
    It links a guest to an episode and includes a rating for the appearance.
    """
    __tablename__ = 'appearances' 

    id = db.Column(db.Integer, primary_key=True) 
    rating = db.Column(db.Integer, nullable=False) 

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    __table_args__ = (
        db.CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating'),
    )

    def __repr__(self):
        """
        Returns a string representation of the Appearance object.
        """
        return f'<Appearance {self.id} | Rating: {self.rating}>'

