from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

def connect_db(aplicacao):
    try:
        data_base=SQLAlchemy(aplicacao)
    except Exception as e:
        print(f'Não foi possível conectar ao DataBase: {e.__cause__}')
    
    return data_base

def create_app():
    app.config.from_object(Config)
    db=connect_db(app)
    return app

