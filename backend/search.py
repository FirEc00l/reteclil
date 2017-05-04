#Da modificare

import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect, abort

def search(request, session, search_key=None):

    if 'user_id' in session:
		logged = session['user_type']
		if logged != 3:
			abort(403)
    else:
		abort(403)

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
            return render_template("home.html", error = "Criterio di ricerca errato", logged=logged)
        else:
            #mostra i risultati
            return render_template("search.html", error = "Criterio di ricerca errato", logged=logged)
            print result
    else:
        return render_template("search.html", logged=logged)
