from flask import Blueprint,jsonify,request
from app.models.users import Users
from extensios import db

user_bp=Blueprint('user',__name__)

@user_bp.route('/user/create',methods=['POST'])
def create_user():
    try:
        data=request.get_json()
        
        nome_usuario=data.get('nome')
        senha_usuario=data.get('senha')
       
        user=Users(nome=nome_usuario,senha=senha_usuario)

        db.session.add(user)
        db.session.commit()

        return jsonify({'message':'Conta Criada'}),200
    
    except Exception as e:
        return jsonify({'erro':str(e.args)}),400
    

@user_bp.route('/users')
def get_usuarios():
    return jsonify({'message':'Lista de usuarios...'})