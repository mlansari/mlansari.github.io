"""The base file for the site"""
import os
# import sqlite3
from flask import Flask, url_for, render_template

APP = Flask(__name__)

@APP.route("/")
def home():
    """Access the home of the website"""
    return render_template("home.html", activePage='home')

@APP.route("/work")
def work():
    """Access the work template"""
    return render_template("work.html", activePage='work')

@APP.route("/contact")
def contact():
    """Access the contact form"""
    return render_template("contact.html", activePage='contact')

@APP.route("/blog")
def blog():
    """Access the blog template"""
    return render_template("home.html", activePage='home')
