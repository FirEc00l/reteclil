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
                SELECT name
                FROM file
                WHERE name LIKE '%{}%'""".format(search_key)

        print query
        result = db.query_db(query)
        
        if result == None:
            return render_template("search.html", logged=logged)
        else:
            #mostra i risultati
            print result
            return render_template("search.html", logged=logged)
    else:
        return render_template("search.html", logged=logged)
