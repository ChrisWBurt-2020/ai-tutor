# backend/app/__init__.py

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from celery import Celery
from flask_cors import CORS
import logging

db = SQLAlchemy()
migrate = Migrate()
api = Api()

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    return celery

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    app.celery = make_celery(app)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    logging.basicConfig(level=logging.INFO)
    handler = logging.FileHandler('app.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    return app

from app import models
