from extensios import db
from app.models.users import Users

class Passwords(db.Model):
    id_senha=db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    password=db.Column(db.String(255),nullable=False)
    

