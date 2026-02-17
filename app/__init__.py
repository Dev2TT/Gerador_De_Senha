from flask import Flask
from config import Config
from app.routes.user_route import user_bp
from extensios import db

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user_bp)

   
    try:
        db.init_app(app)
        print("Banco Conectado com Sucesso!")
    except Exception as e:
        print(f'Não foi possível conectar ao DataBase: {e}')
    
    return app
