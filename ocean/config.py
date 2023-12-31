""" config.py 
--- Configuration 
--- ------------- --- 
--- 20231214 initial commit from Abdelhadi Dyouri (2022) 
-- "How To Structure a Large Flask Application" 
--- ------------- --- 
"""

import os
from dotenv import load_dotenv 

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'ocean.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False