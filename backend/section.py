#FILE EDIT BY Vincenzo Di Pietro

import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect

def section(request, session, section=None):
    db =  utils.pysqlite3()
    query = "SELECT section_name, id_section FROM section"
    sections = db.query_db(query)
    sections_dict = []
    for section in sections:
            query = """SELECT sub_name, id_sub
            FROM sub_section
            WHERE id_section="%s\"""" % str(section[1])
            result = db.query_db(query)
            sections_dict.append( {'name': section[0], 'list': result} )

    sections = sections_dict    
    
    
    if 'user_id' in session:
        logged = session['user_type']
        
    else:
        logged = False
    
    if section==None:
        return render_template("section.html", logged=logged, sections=sections)

    else:
        query = """SELECT *
                FROM file
                WHERE id_sub="%s\"""" % section
        card = db.query_db(query)
        card = card.tolist();
			
        return render_template("section.html", logged=logged, sections=sections, card=card)
            
