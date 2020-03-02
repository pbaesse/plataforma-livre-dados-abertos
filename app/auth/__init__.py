from flask import Blueprint

pb = Blueprint('auth', __name__)

from app.auth import routes
