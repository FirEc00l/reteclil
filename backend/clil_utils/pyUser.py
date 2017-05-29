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


def usrgen(name, surname, default=True, id=None):

    if default:
        id = name[0] + surname + '_' + pswgen('0123456789ABCDEF', 5)
        print id
    else:
        pass
    return


def pswgen(dict, length):
    return ''.join(random.choice(dict) for i in range(length))


usrgen('nicholas', 'sollazzo')
