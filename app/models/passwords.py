from extensios import db
from app.models.users import Users

class Passwords(db.Model):
    id_user=db.Column(db.Integer, db.ForeignKey(Users.id), primary_key=True)
    password=db.Column(db.String(24))
    

