from flask import Blueprint,jsonify,session
from extensios import db
from app.models.passwords import Passwords

password_bp=Blueprint('password',__name__)


@password_bp.route("/password/create")
def create_password():
    return jsonify({'message':'Rota que cria senha'})

@password_bp.route('/passwords',methods=['GET'])
def get_password():

    if 'conta_conectada' not in session or session['conta_conectada'] == None:
        return jsonify({'message':'Nao tem usuario logado'})
    
    id_user_logado=session.get('conta_conectada')

    try:
        query=db.session.execute(db.Query(Passwords.password).filter_by(id_user=id_user_logado)).scalar()
    
    except Exception as e:
        return jsonify({'erro':f'{str(e.args)}'})


    return jsonify({'message':'Conta conectada'})
        