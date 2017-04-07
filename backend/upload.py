from  flask import render_template, url_for, redirect, abort

def upload(request, session):
	if 'user_id' in session:
		if request.method == 'POST':
			pass
		else:
			return render_template("upload.html")
	else:
		abort(403)
