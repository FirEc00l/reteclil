'''
home.py
@author: Nicholas Sollazzo,Alessandro Capici
@version: 1.6
@date: 8/05/17
'''
from flask import render_template
from time import gmtime, strftime
import backend.clil_utils.db as utils
from backend.clil_utils.pyJson import pyJson as pj

DATA = pj('data/data.json')


def home(session):
    # liks :list of dictionary, logged :bool, description :str -> render_template()

    if 'user_id' in session:
        logged = session['user_type']
    else:
        logged = False
    # luogo, indirizzo, desc
    db = utils.pysqlite3()
    c=strftime("%d-%m-%Y %H:%M", gmtime())
    query = "SELECT title, date, description, place, address FROM event WHERE date>'{}'".format(c)
    
    result = db.query_db(query)
    event = []

    if result:
        for events in result:
            event.append({'name': events[0], 'date': events[1],
                          'desc': events[2], 'luogo': events[3], 'indirizzo': events[4]})

    links = DATA.read('links')
    description = DATA.read('description')

    return render_template('home.html', links=links, description=description, logged=logged, event=event)
