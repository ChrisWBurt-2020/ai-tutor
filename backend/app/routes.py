from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.auth import bp
from app.models import User
from app import db

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # Implement login logic
    login_user()
    pass

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
