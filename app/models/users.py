from app import db

class User(db.model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome=db.Column(id.String(150),nullable=False)
    password=db.Column(id.String(25),nullable=False)


    def __repr__(self):
        return f"<name {self.nome}>"