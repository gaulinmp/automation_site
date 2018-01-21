# -*- coding: utf-8 -*-
import os

os_env = os.environ


class Config(object):
    SITE_NAME = "Home"
    SITE_AUTHOR = "Mac Gaulin"
    SITE_DESCRIPTION = "Mold for flask site."
    GOOGLE_ANALYTICS = ''
    SECRET_KEY = os_env.get('SECRET_KEY', 'typeyourrandomstringhere')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # config directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    USE_CDN = True
    USE_USERS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    DB_NAME = 'database.db'
    DBFILE_PATH = os.path.join(Config.APP_DIR, DB_NAME)
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + DBFILE_PATH)


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    USE_CDN = False
    UPLOAD_KEY = 'test'
    WTF_CSRF_ENABLED = False
    DB_NAME = 'dev.db'
    DBFILE_PATH = os.path.join(Config.APP_DIR, DB_NAME)
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + DBFILE_PATH)


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 1  # For faster tests
    WTF_CSRF_ENABLED = False  # Allows form testing
    USE_CDN = False
