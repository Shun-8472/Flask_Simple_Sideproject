import os
import datetime


basedir = os.path.abspath(os.path.dirname(__file__))


def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir, db_name)


class BaseConfig:  # 基本配置
    SECRET_KEY = 'THIS IS MAX'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=14)

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@ip:port/database'
    # SQLALCHEMY_ENGINE_OPTIONS = {
    #     "pool_pre_ping": True,
    #     "pool_recycle": 300,
    #     'pool_timeout': 900,
    #     'pool_size': 10,
    #     'max_overflow': 5,
    # }
    JWT_SECRET_KEY = 'change_key_here'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=30)
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'HOST'
    CACHE_REDIS_PORT = 'PORT'
    CACHE_REDIS_DB = 'DB'


class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@ip:port/database_name'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}