'''
pyUser.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.0
@date: 26/05/17
===========================
pswgen:
permette di generare password lunga n (length) data una list, o stringa, di caratteri (dict)

usergen:
query_db con username inserito senza '_id'. poi cambiare l'username con _id preso dal db

'''

import random

import db as utils


def usrgen(name, surname):

    DB = utils.pysqlite3()

    query = ''' SELECT id_user
                FROM user
            '''

    last_id = DB.query_db(query)

    last_id = int(last_id[-1][-1]) + 1

    id = name[0] + surname + '_' + str(last_id)
    return id


def pswgen(dict, length):
    return ''.join(random.choice(dict) for i in range(length))
