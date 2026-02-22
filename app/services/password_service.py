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
        lista_senhas=[]

        try:
            query=db.session.execute(db.Query(Passwords.password).filter_by(id_user=id)).scalars()
        
        except Exception as e:
            return f'{str(e.args)}'
        
        if query != None:
            for senha in query:
                lista_senhas.append(senha)
            return lista_senhas
        
        return None

        

                

        
        

