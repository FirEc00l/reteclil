def upload(request, session):
	if 'user_id' in session:
		if request.method == 'POST':
			pass
		else:
			return render_template("upload.html")
	else:
		return redirect(url_for('home'))
