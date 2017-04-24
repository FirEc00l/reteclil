import backend.clil_utils.db as utils
from  flask import render_template, url_for, redirect, abort

def upload(request, session):
	if 'user_id' not in session: #togliere not
		db =  utils.pysqlite3()
		if request.method == 'POST':
			pass
		else:
			query = "SELECT section_name, id_section FROM section"
			sections = db.query_db(query)
			print sections
			sections_dict = []
			for section in sections:
				query = """SELECT sub_name, id_sub
				FROM sub_section
				WHERE id_section="%s\"""" % str(section[1])
				result = db.query_db(query)
				sections_dict.append( {'name': section[0], 'list': result} )

			sections = sections_dict
			print sections
			return render_template("upload.html", sections=sections, logged=True)
	else:
		abort(403)
