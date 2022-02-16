import os
os.urandom(24)

class Config:
    SECRET_KEY = 'thisisakey'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:1234@localhost/pitchblog'


    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch'
    SENDER_EMAIL = 'erihngug@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI =os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:1234@localhost/pitches'

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:1234@localhost/pitches_test'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:1234@localhost/pitches'

    DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig,
# 'test':TestConfig
# }
