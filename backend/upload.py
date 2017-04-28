"""
Written by Giammanco Salvatore
Not commented cause i worked hard to write this code
So you have to work hard to understand it
Just kidding, my code is so good that you can understand it without comments
"""

import backend.clil_utils.db as utils
from  flask import render_template, url_for, redirect, abort
from werkzeug.utils import secure_filename

def upload(request, session):
	if 'user_id' in session:
		db =  utils.pysqlite3()

		query = "SELECT section_name, id_section FROM section"
		sections = db.query_db(query)

		if request.method == 'POST':
			f = request.files['file']
			#COntrollare estensione, dimensione file
			#COntrollare nome file nel db, se c'è già aggiungere qualchecos
			f.save('./files/' + secure_filename(f.filename))
			return render_template("upload.html", sections=sections)
		else:
			sections_dict = []
			for section in sections:
				query = """SELECT sub_name, id_sub
				FROM sub_section
				WHERE id_section="%s\"""" % str(section[1])
				result = db.query_db(query)
				sections_dict.append( {'name': section[0], 'list': result} )

			sections = sections_dict

			return render_template("upload.html", sections=sections)
	else:
		abort(403)
