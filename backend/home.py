'''
home.py
@author: Nicholas Sollazzo (Umile)
@version: 1.6
@date: 8/05/17
'''
import backend.clil_utils.db as utils

from flask import render_template

from backend.clil_utils.pyJson import pyJson as pj

DATA = pj('data/data.json')

def home(session):
    # liks :list of dictionary, logged :bool, description :str -> render_template()

    if 'user_id' in session:
        logged = session['user_type']
    else:
        logged = False

    db = utils.pysqlite3()
    query = "SELECT title, date FROM event"
    result = db.query_db(query)

    event = []

    for events in result:
        name = events[0]
        date = events[1]
        event.append({'name': name, 'date': date})

    links = DATA.read('links')
    description = DATA.read('description')

    return render_template('home.html', links=links, description=description, logged=logged, event = event)
