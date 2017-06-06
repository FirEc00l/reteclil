'''
home.py
@author: Nicholas Sollazzo,Alessandro Capici
@version: 1.6
@date: 8/05/17
'''
from time import gmtime, localtime, strftime

from flask import render_template

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

    query = '''SELECT ( julianday(date) - julianday(CURRENT_TIMESTAMP, 'LOCALTIME')) AS diff, title, date, description, place, address
               FROM event
               GROUP BY date
               HAVING diff > 0
               '''

    result = db.query_db(query)

    print result

    event = []

    if result:
        for events in result:
            event.append({'name': events[1], 'date': events[2],
                          'desc': events[3], 'luogo': events[4], 'indirizzo': events[5]})

    links = DATA.read('links')
    description = DATA.read('description')

    return render_template('home.html', links=links, description=description, logged=logged, event=event)
