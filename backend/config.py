import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/ai_tutor_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    CELERY_BROKER_URL = 'redis://localhost:6379/0'

    # Celery Configuration
    BROKER_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    RESULT_BACKEND = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    DEBUG = True
