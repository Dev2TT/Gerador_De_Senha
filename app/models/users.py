from extensios import db

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    nome=db.Column(db.String(150),nullable=False)
    senha=db.Column(db.String(25),nullable=False)


    def __repr__(self):
        return f"<name {self.nome}>"