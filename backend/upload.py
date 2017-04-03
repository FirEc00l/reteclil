def upload(request):
	if 'user_id' in session:
		if request.methon == 'POST':
			pass
		else:
			return render_template("upload.html")
	else:
		return redirect(url_for('home'))