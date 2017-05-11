#Da modificare

import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect, abort

def search(request, session, search_key=None):

    if 'user_id' in session:
        logged = session['user_type']
    else:
        logged=False

    print "test"
    if search_key is not None:
        db = utils.pysqlite3()

        query = """
                SELECT name, description
                FROM file
                WHERE name LIKE '%{}%'""".format(search_key)

        files = db.query_db(query)
        
        if files == None:
            return render_template("search.html", logged=logged, search_key=query)
        else:
            dict_files = []
            for files in files:
                dict_files.append({'name': files[0], 'description': files[1]})
            return render_template("search.html", logged=logged, dict_files=dict_files)
    else:
        return render_template("search.html", logged=logged)
