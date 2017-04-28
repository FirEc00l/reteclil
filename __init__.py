'''
__init__.py
@author: Nicholas Sollazzo
@version: 1.5
@date: 21/04/17
'''

from flask import Flask, request, session, g
import sqlite3
import backend.upload as upload
import backend.login as login
import backend.home as home
import backend.account as account
import backend.manage as manage
import backend.logout as logout
import backend.recovery as recovery

app = Flask(__name__)

@app.route("/")
def route_home():
    return home.home(session)

@app.route("/section/<section>", methods = ['GET','POST'])
def route_section(section):
    return section.section(request)

@app.route("/login", methods = ['GET','POST'])
def route_login():
    return login.login(request, session)

@app.route("/recovery", methods = ['GET','POST'])
def route_recovery():
    return recovery.recovery(request, session)

@app.route("/upload", methods = ['GET','POST'])
def route_upload():
    return upload.upload(request, session)

@app.route("/account", methods = ['GET','POST'])
def route_account():
    return account.account(request, session)

@app.route("/manage", methods = ['GET','POST'])
def route_manage():
    return manage.manage(request)

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
def route_search():
    return search.search(request)

app.secret_key = '\xd7\x9b\xe4\xa2\xa4\x0b\xb5\xd7\xa6}\x1c\xd2\xb6\x1b_\xd9\x12\xdd\xa5\t\xf7\xd5%n'
if __name__ == "__main__":
    app.run()
