'''
__init__.py
@author: Nicholas Sollazzo
@version: 1.4
@date: 21/04/17
'''

from flask import Flask, request, session, g
import sqlite3
import backend.upload as upload
import backend.login as login
import backend.home as home
import backend.account as account
import backend.manage as manage

app = Flask(__name__)

@app.route("/")
def route_home():
    return home.home(session)

@app.route("/section/<section>", methods = ['GET','POST'])
def route_section(section):
    return section(request)

@app.route("/login", methods = ['GET','POST'])
def route_login():
    return login.login(request, session)

@app.route("/recovery", methods = ['GET','POST'])
def route_recovery():
    return recovery(request, session)

@app.route("/upload", methods = ['GET','POST'])
def route_upload():
    return upload.upload(request, session)

@app.route("/account", methods = ['GET','POST'])
def route_account():
    return account(request, session)

@app.route("/manage", methods = ['GET','POST'])
def route_manage():
    return manage(request)

@app.route("/logout")
def route_logout():
    return logout(request)

@app.route("/forum", methods = ['GET','POST'])
def route_forum():
    return forum(request)

@app.route("/forum/<thread_id>", methods = ['GET','POST'])
def route_thread():
    return thread(request)

@app.route("/search/<search_key>", methods = ['GET','POST'])
def route_search():
    return search(request)

if __name__ == "__main__":
    app.run()
