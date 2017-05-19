'''
section.py
@author: Vincenzo Di Pietro
@date: 8/5/17
'''

import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect

def section(request, session, key=None):
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

    if key is None:
        return render_template("section.html", logged=logged, sections=sections, card=None)

    else:

        query = """SELECT name, description
                FROM file
                WHERE id_sub="%s\"""" % str(key)
        result_card = db.query_db(query)
        
        card_dict = []

        if result_card is None :
            return render_template("section.html", logged=logged, sections=sections, card=None)

        else:

            for sub_section in result_card:
                    filename = sub_section[0]
                    file_format = filename.split(".")[-1]
                    card_dict.append( {'title': sub_section[0], 'description' : sub_section[1], 'extension': file_format} )

            card = card_dict

            return render_template("section.html", logged=logged, sections=sections, card=card)
