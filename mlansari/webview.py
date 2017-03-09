"""The base file for the site"""
import os
import sqlite3
from flask import Flask, url_for, render_template, request
from mlansari import app, dbhandler

@app.route("/")
def home():
    """Access the home of the website"""
    return render_template("home.html", activePage='home')

@app.route("/work")
def work():
    """Access the work template"""
    return render_template("work.html", activePage='work')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    """Access the contact form"""
    if request.method == 'GET':
        return render_template("contact.html", activePage='contact')
    elif request.method == 'POST':
        pass        # implement sending an email to me here

@app.route("/blog")
def blog():
    """Access the blog template"""
    db = dbhandler.get_db()
    cur = db.execute('select title, subtitle from blog order by id desc')    # fetch the info from the database
    entries = cur.fetchall()            # perform the built fetch command
    return render_template("blog.html", blog=entries)
