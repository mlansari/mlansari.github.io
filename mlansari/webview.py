"""The base file for the site"""
import os
import sqlite3
from flask import Flask, url_for, render_template, request, redirect, session, abort, flash
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
    cur = db.execute('select title, subtitle, text from blog order by id desc')    # fetch the info from the database
    entries = cur.fetchall()            # perform the built fetch command
    return render_template("blog.html", blog=entries)


# this is a hidden page, used to simply create blog entries
@app.route("/hiddenlogin", methods=['GET', 'POST'])
def login():
    """This is used to login to the blog entry editor, and is in none of the links in the site"""
    error = None
    # handle login attempts
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid Username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Password'
        else:           # this is the success case
            session['logged_in'] = True
            flash("logged in")
            return redirect(url_for('composeBlogEntry'))
    if not session['logged_in']:
        return render_template("login.html", error=error)
    else:
        return redirect(url_for('composeBlogEntry'))


# this is another hidden page, for the actual writing of entries into the blog
@app.route('/compose', methods=['GET'])
def composeBlogEntry():
    """Used to go to the page which is used to compose and process blog entries"""
    if session['logged_in']:
        return render_template("compose.html")
    else:
        return redirect(url_for('login'))
    
@app.route('/add', methods=['POST'])
def addBlogEntry():
    """Used to add the blog entries created in the compose page"""
    if not session['logged_in']:
        abort(401)
    db = dbhandler.get_db()
    db.execute('insert into blog (title, subtitle, text) values (?, ?, ?)',
               [request.form['title'], request.form['subtitle'], request.form['message']])
    db.commit()
    flash("new entry added")

    # for now, log out automatically when you log in (temporary?)
    session['logged_in'] = False

    return redirect(url_for('blog'))