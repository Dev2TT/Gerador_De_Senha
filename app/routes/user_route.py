from flask import Blueprint,jsonify,request

user_bp=Blueprint('user',__name__)

@user_bp.route('/user/create/',methods=['POST'])
def create_user():
    pass

@user_bp.route('/user')
def get_usuarios():
    return jsonify({'message':'Usuarios...'})