from app import db

class Passwords(db.model):
    id=db.Column(db.INTEGER,nullable=False)