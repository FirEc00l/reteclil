'''
__init__.py
@author: Nicholas Sollazzo
@version: 1.2
@date: 6/04/17
'''

from flask import Flask, request, session, g
import sqlite3
import backend.upload as upload
import backend.login as login
import backend.home as home

app = Flask(__name__)

@app.route("/")
def route_home():
    return home.home(session)

@app.route("/section/<section>")
def route_section(section):
    return section(request)

@app.route("/login")
def route_login():
    return login.login(request, session)

@app.route("/recovery")
def route_recovery():
    return recovery(request)

@app.route("/upload")
def route_upload():
    return upload.upload(request,session)

@app.route("/account")
def route_account():
    return account(request)

@app.route("/manage")
def route_manage():
    return manage(request)

@app.route("/logout")
def route_logout():
    return logout(request)

@app.route("/forum")
def route_forum():
    return forum(request)

@app.route("/forum/<thread_id>")
def route_thread():
    return thread(request)

@app.route("/search/<search_key>")
def route_search():
    return search(request)

if __name__ == "__main__":
    app.run()
