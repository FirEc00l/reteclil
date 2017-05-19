# -*- coding: cp1252 -*-
'''
recovery.py
@author: Alesandro Capici
@version: 0.6
@date: 19/05/17
@note: testato ma non funzionante
'''
from flask import render_template
from flask import abort
from flask import url_for
from flask import redirect
from werkzeug.security import generate_password_hash, \
     check_password_hash
import backend.clil_utils.db as utils
#no post reindirizzo template se è e cambio psw


def reset_password(request,session, key=None):
    if 'user_id' in session:
        abort(403)
    else:
        logged = False
        
    if request.method != 'POST':
        db = utils.pysqlite3()
        query = """SELECT key
                   FROM user
                   WHERE key="%s"
                   """ % key
        result=db.query_db(query)
        if result[0][0]==key:
            return redirect(url_for('route_reset_password_key/'+key), code=307)
        else:
            abort(403)
    else:
        print 'garau'
        return redirect(url_for('route_reset_password'))
