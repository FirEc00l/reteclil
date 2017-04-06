'''
__init__.py
@author: Nicholas Sollazzo
@version: 1.2
@date: 6/04/17
'''

from flask import Flask, request, session, g
import sqlite3
import backend.upload as upload

app = Flask(__name__)

@app.route("/")
def route_home():
    home()
    pass

@app.route("/section/<section>")
def route_section(section):
    section(request)
    pass

@app.route("/login")
def route_login():
    login(request)
    pass

@app.route("/recovery")
def route_recovery():
    recovery(request)
    pass

@app.route("/upload")
def route_upload():
    upload.upload(request,session)
    pass

@app.route("/account")
def route_account():
    account(request)
    pass

@app.route("/manage")
def route_manage():
    manage(request)
    pass

@app.route("/logout")
def route_logout():
    logout(request)
    pass

@app.route("/forum")
def route_forum():
    forum(request)
    pass

@app.route("/forum/<thread_id>")
def route_thread():
    thread(request)
    pass

@app.route("/search/<search_key>")
def route_search():
    search(request)
    pass

if __name__ == "__main__":
    app.run()
