from app import app
from models import db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from datetime import date

def seed():
    with app.app_context():
        print("Dropping all tables...")
        db.drop_all()
        print("Creating all tables...")
        db.create_all()
        
        user = User(username='admin')
        user.set_password('password')
        db.session.add(user)
        print("Added user: admin")
        
        guests = [
            Guest(name='John Doe', occupation='Actor'),
            Guest(name='Jane Smith', occupation='Comedian'),
            Guest(name='Bob Johnson', occupation='Musician')
        ]
        db.session.add_all(guests)
        print("Added guests:", [g.name for g in guests])
        
        episodes = [
            Episode(date=date(2025, 6, 1), number=1),
            Episode(date=date(2025, 6, 2), number=2)
        ]
        db.session.add_all(episodes)
        print("Added episodes:", [e.number for e in episodes])
        
        appearances = [
            Appearance(rating=4, guest_id=1, episode_id=1),
            Appearance(rating=5, guest_id=2, episode_id=1),
            Appearance(rating=3, guest_id=3, episode_id=2)
        ]
        db.session.add_all(appearances)
        print("Added appearances:", [a.rating for a in appearances])
        
        print("Committing session...")
        db.session.commit()
        print("Seed completed.")

if __name__ == '__main__':
    seed()