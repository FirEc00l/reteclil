#Da modificare

import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect

def search(request, session):
    print request.method
    if request.method=='GET':
        print "azz"
        db = utils.pysqlite3()
        print "azz2"
        query = """
                SELECT name
                FROM file
                WHERE name LIKE '%entry%'""" % request.form['search_key']
        print query
        result = db.query_db(query)

        if result == None:
            return render_template("home.html", error = "Criterio di ricerca errato")
        else:
            #mostra i risultati
            return render_template("search.html", error = "Criterio di ricerca errato")
            print result
            
    print "render search.html"
    return render_template("search.html")
