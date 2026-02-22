from flask import Blueprint,jsonify,request,session
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
    

@user_bp.route('/users',methods=['GET'])
def get_usuarios():
    try:
        usuarios=db.session.execute(db.select(Users).order_by(Users.nome)).all()
    except Exception as e:
        return jsonify({'message':f'{str(e.__cause__)}'})

    return jsonify({'Usuarios':f'{usuarios}'})

@user_bp.route('/user/<int:id_user>',methods=['GET'])
def get_user_by_id(id_user):
    try:
        user=db.session.execute(db.Query(Users.nome).filter_by(id=id_user)).scalar()
    
    except Exception as e:
        return jsonify({'message':f'{str(e.args)}'})
    
    if user:
        return jsonify({'Usuario':user})
    
    return jsonify({'message':f'Usuario com id: {str(id_user)} nao encontrado.'})


@user_bp.route('/user/<string:id_user>',methods=['DELETE'])
def delete_user(id_user):
    id_user=int(id_user)

    try:
        user=db.session.execute(db.Query(Users).filter_by(id=id_user)).scalar()
    
    except Exception as e:
        return jsonify({'erro':f'{str(e.args)}'})
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message':f'Usuario com {str(id_user)} foi deletado do banco.'})
    
    return jsonify({'message':'Usuario nao foi encontrado'})


@user_bp.route('/user/<string:id_user>',methods=['PUT'])
def atualiza_usuario(id_user):
    id_user=int(id_user)

    try:
        user=db.session.execute(db.Query(Users).filter_by(id=id_user)).scalar()
    
    except Exception as e:
        return jsonify({'erro':f'{str(e.args)}'})
    
    if user:
        data=request.get_json()

        novo_nome= data.get('nome')
        nova_senha=data.get('senha')
        
        if novo_nome != None:
            user.nome = str(novo_nome)

        if nova_senha != None:
            user.senha=str(nova_senha)    


        db.session.commit()

        return jsonify({'Sucesso':f'Usuario com id {str(id_user)} foi atualizado'})

    return jsonify({'message':f'Usuario com id {str(id_user)} nao localizado.'})

@user_bp.route('/user/login/', methods=['POST'])
def login():
    try:
        data=request.get_json()
        
    except Exception as e:
        return jsonify({'message':'JSON nao encontrado'})
    
    username=data.get('username')
    senha=data.get('senha')
    
    try:
        user=db.session.execute(db.Query(Users).filter_by(nome=username)).scalar()

    except Exception as e:
        return jsonify({'erro':f'{str(e.args)}'})
    
    if user.nome == username:
        if user.senha == senha:
            print("LOGIN salvou:", session['conta_conectada'])
            session['conta_conectada']=user.id
            return jsonify({'Message':'logado!'})
        
        return jsonify({'message':'Senha Incorreta'}),404
    
    return jsonify({'message':'usuario nao encontrado no banco'}),200

@user_bp.route('/user/logout')
def logout():
    if session.get('conta_conectada') != None:
        try:
            session['conta_conectada']=None
            return jsonify({'logout':'Deslogado'})
        
        except Exception as e:
            return jsonify({'erro':f'{str(e.args)}'})

    return jsonify({'logout':'Nao possui conta conectada para deslogar.'})

    