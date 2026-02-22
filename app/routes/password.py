from flask import Blueprint,jsonify,session,request
from extensios import db
from app.models.passwords import Passwords
from app.services.password_service import PasswordService

password_bp=Blueprint('password',__name__)


@password_bp.route("/password/create/<string:senha>",methods=['POST'])
def create_password(senha):    
    if 'conta_conectada' not in session or session['conta_conectada'] == None:
        return jsonify({'message':'Nao tem usuario logado'})

    try:
        strong_password=PasswordService.create_password(senha)
        
        if strong_password == None or strong_password == '':
            return jsonify({'erro':'senha_vazia'})

        password_user=Passwords(
            id_user=int(session['conta_conectada']),
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

@password_bp.route('/password/<int:id_senha>',methods=['DELETE'])
def delete_password(id_senha):
    if 'conta_conectada' not in session or session['conta_conectada'] == None:
        return jsonify({'message':'usuario nao logado'})
    
    try:
        query=PasswordService.delete_password(id_senha)
        return jsonify(query),200
        
    except Exception as e:
        return jsonify({'error': str(e.args)}),400

@password_bp.route('/password/<int:id_senha>/<string:nova_senha>',methods=['PUT'])
def atualiza_senha(id_senha,nova_senha):
    if 'conta_conectada' not in session or session['conta_conectada'] == None:
        return jsonify({'message':'usuario nao logado'})
    
    try:
        atualiza=PasswordService.atualiza_senha(id_senha,nova_senha)
        return jsonify(atualiza),200
    
    except Exception as e:
        return jsonify({'erro':str(e.args)})
     