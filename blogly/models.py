import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Blog_Users(db.Model):
    """user profile."""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.Text(50),
                           nullable=False)
    
    last_name = db.Column(db.Text(50),
                           nullable=False)
    
    image_url = db.Column(db.Text, nullable=True)

    posts = db.relationship('Post', backref='user', cascade="all, delete-orphan")

    @property
    def full_name(self):
        """full name"""
        return f"{self.first_name} {self.last_name}"
    
class Post(db.model):
     """post"""
     __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    @property
    def friendly_date(self):
        """friendly date"""
        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

# Path: blogly/app.py    

