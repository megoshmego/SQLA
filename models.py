from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class blog_user(db.Model):
    """user profile."""

    __tablename__ = 'user'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(50),
                           nullable=False)
    
    last_name = db.Column(db.String(50),
                           nullable=False)
    
    image = db.Column(db.LargeBinary, nullable=True)
    

