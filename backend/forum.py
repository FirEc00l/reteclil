'''
forum.py
@author: Vincenzo Di Pietro
@date: 19/05/17
'''

import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect

def forum(request, session):

    return render_template("forum.html")
