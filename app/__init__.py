from flask import Flask
from common.db import db
from common.ma import ma
from common.jwt import jwt
from common.mg import migrate
from common.rd import cache
from .config.config import config

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)

    return app