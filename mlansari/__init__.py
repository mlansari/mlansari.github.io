"""Initialization information"""
# Imports for the project as a whole
# from .mlansari import APP
import sqlite3
import logging
from flask import Flask, request, url_for, g

#########
# Setup #
#########
# no need to do anything here rn.  It's not exactly complicated
logger = logging.getLogger("BaseLog")

################
# app Creation #
################
app = Flask(__name__)

# need to be imported after app creation
from mlansari import config, webview

app.config.from_object(config.DevConfig)            # comment this to run live
# app.config.from_object(config.LiveConfig)         # uncomment this to run live

##########################
# Database Functionality #
##########################
## Note that the database exists for the purpose of blog functionality

# def init_db():
#     """Initialize the database into existence"""
#     db = get_db()                       # fetch the database 
#     with app.open_resource('schema.sql', 'r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()

# @app.cli.command('initdb')
# def initdb_command():
#     """Initialize the database from terminal"""
#     dbhandler.init_db()           # this command can be used by writing "flask initdb"
#     print("Database initialized")

# def get_db():
#     """Fetches the existing database (implemented in sqlite3) for the Flask object"""
#     db = getattr(g, '_database', None) # set db to None if no database exists
#     if db is None:
#         db = g._database = sqlite3.connect(app.config['DATABASE'])
#         db.row_factory = sqlite3.Row
#     return db   # return the new or generated database

# @app.teardown_appcontext
# def close_connection(exception):
#     """Close the connection to the database when the app shuts down"""
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()          # if there is an existent database connection, close it
