from extensios import db
from app.models.users import Users

class Passwords(db.Model):
    id_senha=db.Column(db.Integer, primary_key=True,auto_increment=True)
    id_user=db.Column(db.ForeignKey(Users.id), primary_key=True)
    password=db.Column(db.String(255))
    

