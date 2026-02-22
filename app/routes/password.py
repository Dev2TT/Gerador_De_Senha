from flask import Blueprint,jsonify,session
from extensios import db
from app.models.passwords import Passwords
from app.services.password_service import PasswordService

password_bp=Blueprint('password',__name__)


@password_bp.route("/password/create/<string:senha>",methods=['POST'])
def create_password(senha):    
    id_usuario=session['conta_conectada']

    if not id_usuario:
        return jsonify({'message':'Nenhum usuario logado'})
    
    try:
        strong_password=PasswordService.create_password(senha)
        
        if strong_password == None or strong_password == '':
            return jsonify({'erro':'senha_vazia'})

        password_user=Passwords(
            id_user=id_usuario,
            password=strong_password
            )
        
        db.session.add(password_user)
        db.session.commit()

        return jsonify({'message':'password added'})

    except Exception as e:
        return jsonify({'erro':f'{str(e.args)}'})
    
    

@password_bp.route('/passwords',methods=['GET'])
def get_password():

    if 'conta_conectada' not in session or session['conta_conectada'] == None:
        return jsonify({'message':'Nao tem usuario logado'})
    
    id_user_logado=session.get('conta_conectada')

    passwords=PasswordService.get_passwords(id_user_logado)

    if passwords == None:
        return jsonify({'message':'Nenhuma senha associada a esse usuario'})
    
    return jsonify({'Passwords':passwords})
        