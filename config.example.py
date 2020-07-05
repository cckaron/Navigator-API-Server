class Config(object):
    #Base flask config
    DEBUG = True
    DEVELOPMENT = True
    HOST = '0.0.0.0'
    PORT = '8080'

    #db config
    DB_SERVER = 'YOUR_DB_SERVER'
    DB_PORT = 'YOUR_DB_PORT'
    DB_NAME = 'YOUR_DB_NAME'
    DB_USER = 'YOUR_DB_ADMIN'
    DB_PASSWORD = 'YOUR_DB_PASSWORD'

    #Connexion
    CONNEXION_DIR = './'
    CONNEXION_YAML = 'swagger.yaml'
    
    #SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):         # Note: all caps
        return 'mysql+pymysql://{}:{}@{}:{}/navigator'.format(self.DB_USER, self.DB_PASSWORD, self.DB_SERVER, self.DB_PORT)

class ProductionConfig(Config):
    """Uses production database server."""
    DEVELOPMENT = False
    DEBUG = False
    DB_SERVER = ''

class AwsConfig(Config):
    """Uses AWS rds server."""

class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True

class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    DATABASE_URI = 'sqlite:///:memory:'