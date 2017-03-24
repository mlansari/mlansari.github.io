"""Holder for various configuration options for my website"""
import os
from . import app

class Config(object):
    """A blank object used to define default configuration properties for the program"""
    DEBUG = False
    TESTING = False
    DATABASE = os.path.join(app.root_path, 'mlansari.db')
    SECRET_KEY=None         # This needs to be set

class DevConfig(Config):
    """The object version used for debugging, versus the production config"""
    DEBUG = True
    USERNAME='testing'
    PASSWORD='password'
    SECRET_KEY="AEIOU"

class LiveConfig(Config):
    """The object version used for the actual run of the site"""
    # It's up to you to decide what config values to use for this
    pass
