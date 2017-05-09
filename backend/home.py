'''
home.py
@author: Nicholas Sollazzo
@version: 1.6
@date: 8/05/17
'''
from flask import render_template

from backend.clil_utils.pyJson import pyJson as pj

DATA = pj('data/data.json')

def home(session):
    # liks :list of dictionary, logged :bool, description :str -> render_template()

    if 'user_id' in session:
        logged = session['user_type']
    else:
        logged = False


    links = DATA.read('links')
    description = DATA.read('description')

    return render_template('home.html', links=links, description=description, logged=logged)
