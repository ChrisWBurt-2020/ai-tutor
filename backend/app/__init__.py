# app/__init__.py
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

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['RESULT_BACKEND']
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
    app.config.from_object('config.Config')
    CORS(app)
    if 'CELERY_BROKER_URL' not in app.config:
        app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'  # Default value
    if 'RESULT_BACKEND' not in app.config:
        app.config['RESULT_BACKEND'] = 'redis://localhost:6379/0'

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    app.celery = make_celery(app)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

from app import models
