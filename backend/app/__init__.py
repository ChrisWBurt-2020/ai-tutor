from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import Config
from celery import Celery
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
api = Api()
celery = Celery(__name__)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object('config.Config')
    CORS(app)
    if 'CELERY_BROKER_URL' not in app.config:
        app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'  # Default value
    

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    app.celery = celery  # Attach celery to the app

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

from app import models
