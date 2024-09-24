# backend/app/config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://ai_tutor_user:StrongPassword123@localhost/ai_tutor_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL') or 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND') or 'redis://localhost:6379/0'
    DEBUG = True
