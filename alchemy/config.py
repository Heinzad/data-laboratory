"""config.py application configuration 
-- reference: Miguel Grinberg (2018). Flask Web Development: Developing Web Applications with Python. O'Reilly. 

-- 20231209 initial commit: Adam Heinz 
""" 

from os import path as os_path
from os import environ as os_environ

basedir = os_path.abspath(os_path.dirname(__file__))


class Config:
    """Base configurations super class"""
    SECRET_KEY = os_environ.get('SECRET_KEY') or 'D0n`t~kommit~2~sauce~k0ntr0l-y`all'
    MAIL_SERVER = os_environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os_environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os_environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os_environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os_environ.get('MAIL_PASSWORD')
    ALCHEMY_MAIL_SUBJECT_PREFIX = '[Alchemy]'
    ALCHEMY_MAIL_SENDER = 'Alchemy Admin <alchemy@example.com>'
    ALCHEMY_ADMIN = os_environ.get('ALCHEMY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app): 
        pass


class DevelopmentConfig(Config): 
    """Development environment configuration subclass""" 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os_environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os_path.join(basedir, 'alchemydb-dev.sqlite')
    

class TestingConfig(Config):
    """Test environment configuration subclass"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os_environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os_path.join(basedir, 'alchemydb-test.sqlite')


class ProductionConfig(Config):
    """Production environment configuration subclass"""
    SQLALCHEMY_DATABASE_URI = os_environ.get('PROD_DATABASE_URL') or \
        'sqlite:///' + os_path.join(basedir, 'alchemydb-prod.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig, 
    'default': DevelopmentConfig 
}


