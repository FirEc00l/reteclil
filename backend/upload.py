"""
Written by Giammanco Salvatore
Not commented cause i worked hard to write this code
So you have to work hard to understand it
Just kidding, my code is so good that you can understand it without comments
"""

import backend.clil_utils.db as utils
import calendar
from  flask import render_template, url_for, redirect, abort, request
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

def upload(request, session):
	if 'user_id' in session:
		logged = session['user_type']
		if logged < 2:
			abort(403)

		db = utils.pysqlite3()
		query = "SELECT section_name, id_section FROM section"
		sections = db.query_db(query)

		if request.method == 'POST':
                        title = name = request.form.get('title', None)
                        print "title is null"
                        if title is None:
                                f = request.files['file']
                                
                                if f and allowed_file(f.filename):
                                        '''Controllare nome file nel db, se ce gia aggiungere qualchecos
                                        query = "SELECT id_file FROM file WHERE name = '%s'" % f.filename
                                        result = db.query_db(query)'''

                                        id_sub = request.form.get('sub_sec')
                                        id_user = session['user_id']
                                        description = request.form['desc']
                                        
                                        query = "INSERT INTO file VALUES(NULL, '%s','%s','%s', '%s')" % (f.filename, id_user, id_sub, description)
                                        db.query_db(query)
                                        f.save('./static/files/' + secure_filename(f.filename))


                                        print "inserito un file giusto"
                                        return redirect(url_for('route_upload', sections=sections, logged=logged, success = True))
                                        #return render_template("upload.html", sections=sections, logged=logged, success = True)
                                        #return "success"
                                else:
                                        return render_template("upload.html", sections=sections, logged=logged, success = False)
                                        #return "error"
                        else:
                                title = request.form['title']
                                place = request.form['place']
                                address = request.form['address']
                                date = request.form['event_date']
                                time = request.form['event_time']
                                datetime = date + time
                                description = request.form['description']
                                id_user = session['user_id']

                                abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}

                                day = date.split(' ')[0]
                                if day < 10:
                                        day = '0' + day
                                month = date.split(' ')[1]
                                month = month[0:3]
                                month = abbr_to_num[month]
                                year = date.split(' ')[2]
                                year = year[2:]

                                datetime = str(day) + "-" + str(month) + "-" + str(year) + " " + str(time)
                                
                                query = "INSERT INTO event VALUES(NULL, '%s', '%s', '%s', '%s', '%s', '%s')" % (title, datetime, description, place, address, id_user)
                                db.query_db(query)
                                print "inserito evento giusto"
                                return render_template("upload.html", sections=sections, logged=logged, success = True)
                                #return "success"
                                
		else:
			sections_dict = []
			for section in sections:
				query = """SELECT sub_name, id_sub
				FROM sub_section
				WHERE id_section="%s\"""" % str(section[1])
				result = db.query_db(query)
				sections_dict.append( {'name': section[0], 'list': result} )

			sections = sections_dict
			print "return pagina vuota"
			#return redirect(url_for('route_upload', sections=sections, logged=logged, success = True))
			return render_template("upload.html", sections=sections, logged=logged)
	else:
		abort(403)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
