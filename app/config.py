class Config(object):
    TESTING = False

class ProductionConfig(Config):
    TESTING = True
    DB_NAME = "quack"
    DB_HOST = "89.208.84.222"
    DB_USER = "quack"
    DB_PASS = "ewTe6pEFyIK"
    SQLALCHEMY_DATABASE_URI = 'postgres://quack:ewTe6pEFyIK@89.208.84.222/quack'

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
