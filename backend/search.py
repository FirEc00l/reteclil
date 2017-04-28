#Da modificare

import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect

def search(request, session):

    if request.method='POST':
        db = utils.pysqlite3()
        query = """
                SELECT name
                FROM file
                WHERE name LIKE '%entry%'""" % request.form['search_key']
        result = db.query_db(query)

        if result == None:
            return render_template("home.html", error = "Criterio di ricerca errato")
        else:
            #mostra i risultati
            print result
    else:
        return render_template("home.html", error = "Criterio di ricerca errato")
