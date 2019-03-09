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
