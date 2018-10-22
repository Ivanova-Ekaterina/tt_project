class Config(object):
    TESTING = False


class ProductionConfig(Config):
    TESTING = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
