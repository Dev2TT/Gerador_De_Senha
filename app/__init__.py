from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    try:
        db=SQLAlchemy(app)

    except Exception as e:
        print(f'Não foi possível conectar ao DataBase: {e.__cause__}')
    
    return app