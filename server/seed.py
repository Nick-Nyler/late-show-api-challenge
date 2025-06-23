from .app import create_app 

from server.models import db, User, Guest, Episode, Appearance
from datetime import date 

def seed():
    """
    Function to seed the database with initial data.
    This includes dropping existing tables, creating new ones,
    and populating them with sample users, guests, episodes, and appearances.
    """
    app = create_app()
    
    with app.app_context():
        print("Starting database seeding...")

        db.drop_all()
        print("Dropped all existing tables.")

        db.create_all()
        print("Created all new tables.")

        print("Seeding users...")
        user = User(username="admin")
        user.set_password("password")
        db.session.add(user) 
        db.session.commit() 
        print(f"Added user: {user.username}")

        print("Seeding guests...")
        guest1 = Guest(name="John Doe", occupation="Actor")
        guest2 = Guest(name="Jane Smith", occupation="Comedian")
        guest3 = Guest(name="Chris Rock", occupation="Comedian")
        guest4 = Guest(name="Oprah Winfrey", occupation="TV Host")
        db.session.add_all([guest1, guest2, guest3, guest4]) 
        db.session.commit()
        print("Added sample guests.")

        print("Seeding episodes...")
        episode1 = Episode(date=date(2025, 6, 1), number=101)
        episode2 = Episode(date=date(2025, 6, 2), number=102)
        episode3 = Episode(date=date(2025, 6, 3), number=103)
        db.session.add_all([episode1, episode2, episode3]) 
        db.session.commit() 
        print("Added sample episodes.")

        print("Seeding appearances...")
       
        appearance1 = Appearance(rating=4, guest_id=guest1.id, episode_id=episode1.id)
        appearance2 = Appearance(rating=5, guest_id=guest2.id, episode_id=episode2.id)
        appearance3 = Appearance(rating=3, guest_id=guest3.id, episode_id=episode1.id)
        appearance4 = Appearance(rating=5, guest_id=guest4.id, episode_id=episode3.id)
        db.session.add_all([appearance1, appearance2, appearance3, appearance4]) 
        db.session.commit() 
        print("Database seeding completed successfully!")

if __name__ == '__main__':
    seed()

