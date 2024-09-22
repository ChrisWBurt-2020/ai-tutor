from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import users, lessons
from app import tasks  # Import tasks at the bottom
