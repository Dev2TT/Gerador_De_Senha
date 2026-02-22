from random import randint
from extensios import db
from app.models.passwords import Passwords


class PasswordService:

    @staticmethod
    def create_password(senha:str):
        senha.lower()
        password=''
        lista=[]
        numeros=[]

        for letter in senha:
            lista.append(letter)
        
        for c in range(0,len(lista)):
            inteiro=randint(0,10)
            numeros.append(inteiro)
        
        lista.sort(reverse=True)

        for c in range(0,len(lista)):
            password+=lista[c]
            password+=str(numeros[c])
        
        return password

    @staticmethod
    def get_passwords(id):
        senhas={}

        try:
            query=db.session.execute(db.Query(Passwords).filter_by(id_user=id)).scalars()
        
        except Exception as e:
            return f'{str(e.args)}'
        
        if query != None:
            for senha in query:
                senhas[senha.id_senha] = senha.password
            return senhas
        
        return None
    
    @staticmethod
    def delete_password(id):
        try:
            senha=db.session.execute(db.Query(Passwords).filter_by(id_senha=id)).scalar()
            db.session.delete(senha)
            db.session.commit()

        except Exception as e:
            return {'message':f'senha com esse id [{id}] nao foi encontrada'}
        
        return {'message':f'senha com id {id} foi apagada'}



        

                

        
        

