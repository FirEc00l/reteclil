"""
Written by Giammanco Salvatore
Not commented cause i worked hard to write this code
So you have to work hard to understand it
Just kidding, my code is so good that you can understand it without comments
"""

from  flask import render_template, url_for, redirect, abort, request

def credits(session):
    if 'user_id' in session:
        logged = session['user_type']
    else:
        logged = False
    return render_template("credits.html", logged=logged)
