from app import connect_db
from strong_password import StrongPassword
db=connect_db()

class User(db.model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome=db.Column(id.String(150),nullable=False)
    password=db.Column(id.String(25),nullable=False)
    id_password= db.column(db.Integer, db.ForeignKey(StrongPassword.id))


    def __repr__(self):
        return f"<name {self.nome}>"