'''
forum.py
@author: Vincenzo Di Pietro
@date: 19/05/17
'''

import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect

def forum(request, session):
    if 'user_id' in session:
		logged = session['user_type']
    else:
        abort(403)
		
    result_dict = []

    db =  utils.pysqlite3()
    query = "SELECT id_thread, title, id_user, name, surname FROM thread NATURAL JOIN user"
    result = db.query_db(query)

    if result is None :
        threads = None
        return render_template("forum.html", logged=logged, threads=threads)

    else:
        for thread in result:
                        result_dict.append( {'id_thread': thread[0], 'title' : thread[1], 'id_user' : thread[2], 'name' : thread[3], 'surname' : thread[4]} )
        threads = result_dict

        print threads

        return render_template("forum.html", logged=logged, threads=threads)

    '''
    if request.method=='POST' :

    query = """INSERT INTO table_name
               VALUES (NULL, %s, , ,%s);""" %
    
    '''
