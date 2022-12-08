from flask_mongoengine import MongoEngine

from pymongo import monitoring
from src.utility.logs import CommandLogger

db = MongoEngine()

def start_db(app):
    db.init_app(app)

monitoring.register(CommandLogger())