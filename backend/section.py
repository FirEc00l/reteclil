import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect

def section(request, session, section=None):
    
    
    
    if 'user_id' in session:
        logged = session['user_type']
        
    else:
        logged = False
    
    if section==None:
        return render_template("section.html", logged=logged)

    else:
        db =  utils.pysqlite3()
        query = """SELECT *
                FROM Section
                WHERE Section.id_section="%s\"""" % section
        result = db.query_db(query)

        return render_template("section.html", logged=logged, result=result)
            
