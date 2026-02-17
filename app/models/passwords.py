from extensios import db

class Passwords(db.Model):
    id=db.Column(db.INTEGER,nullable=False)
    password=db.Column(db.String(24))