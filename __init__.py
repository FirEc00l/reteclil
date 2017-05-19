'''
__init__.py
@author: Nicholas Sollazzo,Alessadro Capici(pivccole modifiche)
@version: 1.8
@date: 10/05/17
'''

from flask import Flask
from flask import request
from flask import session
from flask import g
from flask import render_template

import sqlite3

import backend.home as home
import backend.section as section
import backend.login as login
import backend.recovery as recovery
import backend.reset_password as reset_password
import backend.upload as upload
import backend.account as account
import backend.manage as manage
import backend.logout as logout
import backend.forum as forum
import backend.thread as thread
import backend.search as search

app = Flask("__name__")

app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

@app.errorhandler(403)
def permission_denied(e):
    if 'user_id' in session:
        logged = session['user_type']
    else:
        logged = False
    return render_template('403.html', logged=logged), 403

@app.errorhandler(404)
def page_not_found(e):
    if 'user_id' in session:
        logged = session['user_type']
    else:
        logged = False
    return render_template('404.html', logged=logged), 404

@app.errorhandler(413)
def too_long(e):
    return "request_too_long", 413

@app.route("/")
def route_home():
    return home.home(session)

@app.route("/section/<key>", methods = ['GET','POST'])
def route_section_key(key):
    return section.section(request, session, section=key)

@app.route("/section", methods = ['GET','POST'])
def route_section():
    return section.section(request, session)

@app.route("/login", methods = ['GET','POST'])
def route_login():
    return login.login(request, session)

@app.route("/recovery", methods = ['GET','POST'])
def route_recovery():
    return recovery.recovery(request, session)

@app.route("/reset_password", methods = ['GET','POST'])
def route_reset_password():
    return reset_password.reset_password(request, session)

@app.route("/reset_password/<key>", methods = ['GET','POST'])
def route_reset_password_key(key):
    return reset_password.reset_password(request, session , key=key)

@app.route("/upload", methods = ['GET','POST'])
def route_upload():
    return upload.upload(request, session)

@app.route("/account", methods = ['GET','POST'])
def route_account():
    return account.account(request, session)

@app.route("/manage", methods = ['GET','POST'])
def route_manage():
    return manage.manage(request, session)

@app.route("/logout")
def route_logout():
    return logout.logout(session)

@app.route("/forum", methods = ['GET','POST'])
def route_forum():
    return forum.forum(request)

@app.route("/forum/<thread_id>", methods = ['GET','POST'])
def route_thread():
    return thread.thread(request)

@app.route("/search/<search_key>", methods = ['GET','POST'])
def route_search_key(search_key):
    return search.search(request, session, search_key)

@app.route("/search", methods = ['GET','POST'])
def route_search():
    return search.search(request, session)

app.secret_key = '\xd7\x9b\xe4\xa2\xa4\x0b\xb5\xd7\xa6}\x1c\xd2\xb6\x1b_\xd9\x12\xdd\xa5\t\xf7\xd5%n'
if __name__ == "__main__":
    app.run()
