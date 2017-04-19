from  flask import render_template, url_for, redirect, abort

def upload(request, session):
	if 'user_id' not in session:
		if request.method == 'POST':
			pass
		else:
			sections = ["Section 1", "Section 2", "Section 3"] #Prenderle dal db
			return render_template("upload.html", sections=sections)
	else:
		abort(403)
