# backend/app/celery_worker.py

from app import create_app

app = create_app()
celery = app.celery
