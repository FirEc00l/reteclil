'''
__init__.py
@author: Nicholas Sollazzo
@version: 1.1
@date: 7/04/17
'''
from flask import render_template
import json

def home(session):
    # liks :list of dictionary, logged :bool, description :str -> render_template()

    if 'user_id' in session:
        logged = True
    else:
        logged = False

    with open('data/data.json') as data_file:
        data_str = data_file.read()
        links = json.loads(data_str)['links']
        description = json.loads(data_str)['description']


    return render_template('home.html', links=links, description=description)
