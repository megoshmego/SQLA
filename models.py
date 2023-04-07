from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Blog_Users(db.Model):
    """user profile."""

    __tablename__ = 'blog_users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(50),
                           nullable=False)
    
    last_name = db.Column(db.String(50),
                           nullable=False)
    
    image_url = db.Column(db.String, nullable=True)

    @property
    def full_name(self):
        """full name"""
        return f"{self.first_name} {self.last_name}"

    

