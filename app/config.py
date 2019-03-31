class Config(object):
   TESTING = False

class ProductionConfig(Config):
    TESTING = False
    DB_NAME = "track"
    DB_HOST = "localhost"
    DB_USER = "ekaterina"
    DB_PASS = ""


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
