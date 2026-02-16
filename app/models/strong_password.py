from app import connect_db
db=connect_db()

class StrongPassword(db.model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    length_password=db.Column(db.Integer,nullable=False)
    letter_password=db.Column(db.String(10),nullabel=False)
    special_character_password=db.Column(db.String(2),nullable=False)
    password_completed=db.Column(db.String(24))


