import os
basedir = os.path.abspath(os.path.dirname(__file__))
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

class Config(object):
    DATABASE_URL = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    CSRF_ENABLED = True
    GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET')

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
