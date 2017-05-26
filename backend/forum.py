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

    else :
        logged = None

    result_dict = []

    db =  utils.pysqlite3()
    query = "SELECT * FROM post"
    result = db.query_db(query)

    print result

    if result == None :
        threads = None
        return render_template("forum.html", logged=logged, threads=threads)

    else:
        for thread in result:
                        filename = sub_section[0]
                        file_format = filename.split(".")[-1]
                        result_dict.append( {'id_post': thread[0], 'title' : thread[1], 'content' : thread[2], 'date_post' : thread[3], 'id_user' : thread[4], 'id_thread' : thread[5], 'extension': file_format} )
        threads = result_dict

        return render_template("forum.html", logged=logged, threads=threads)
