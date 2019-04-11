class Config(object):
   TESTING = False

class ProductionConfig(Config):
    TESTING = False
    DB_NAME = "track"
    DB_HOST = "localhost"
    DB_USER = "ekaterina"
    DB_PASS = ""
    SQLALCHEMY_DATABASE_URI = 'postgres://quack:ewTe6pEFyIK@192.168.18.73/quack'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DB_NAME = "track_test"
    DB_HOST = "localhost"
    DB_USER = "ekaterina"
    DB_PASS = ""
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'katyna1816@gmail.com'
    MAIL_PASSWORD = 'ester_95'
    SQLALCHEMY_DATABASE_URI = 'postgres://ekaterina:@localhost/track_orm'
