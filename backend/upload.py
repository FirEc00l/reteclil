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
		logged = session['user_type']
		db =  utils.pysqlite3()

		query = "SELECT section_name, id_section FROM section"
		sections = db.query_db(query)

		if request.method == 'POST':
			f = request.files['file']
			#Controllare estensione, dimensione file
			ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
			if f and allowed_file(f.filename):
				f.save('./files/' + secure_filename(f.filename))
			else:
				return "error"
			#Controllare nome file nel db, se ce gia aggiungere qualchecos


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

			return render_template("upload.html", sections=sections, logged=logged)
	else:
		abort(403)
