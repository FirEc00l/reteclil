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

    if key:
    
        db = utils.pysqlite3()
        query = """SELECT key
                       FROM user
                       WHERE key="%s"
                       """ % key
        result=db.query_db(query)
        print result
        
        if result[0][0]==key:
            if request.method == 'POST':
                #cambio psw
                return render_template('reset_password.html', logged=logged, success="sdfser")
            else:
                return render_template('reset_password.html', logged=logged, key=key)
        else:
            abort(403)
    else:
        return redirect(url_for("route_recovery"))
            
