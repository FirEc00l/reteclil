'''
login.py
@author: Vincenzo Di Pietro ,Alesandro Capici
@date: 8/5/17
'''

#from flask import Flask
import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect
from werkzeug.security import generate_password_hash, \
     check_password_hash
#app = Flask(__name__)
#@app.route("/login", methods=['GET', 'POST'])

def login(request, session):

    if 'user_id' not in session:

        if request.method=='POST' :

            print request.form['username']
            db =  utils.pysqlite3()
            query = """SELECT username, password, id_user, user_type
                       FROM User
                       WHERE User.username="%s\"""" % request.form['username']
            result = db.query_db(query)

            print request.form['password']
            print result[0][1]
            
            if result==None :
                return render_template("login.html", error = "Nome utente o password errata", logged=False)
        
            elif check_password_hash(result[0][1],request.form['password']):
                session['user_id'] = result[0][2]
                session['user_type'] = result[0][3]
                return redirect(url_for('route_home'))

            else:
                return render_template("login.html", error = "Nome utente o password errata", logged=False)
        else:
            return render_template("login.html", logged=False)
    return redirect(url_for('route_home'))
