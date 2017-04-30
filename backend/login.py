#from flask import Flask
import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect
#app = Flask(__name__)
#@app.route("/login", methods=['GET', 'POST'])

def login(request, session):

    if 'user_id' not in session:

        if request.method=='POST' :


            db =  utils.pysqlite3()
            query = """SELECT username, password, id_user, user_type
                       FROM User
                       WHERE User.username="%s\"""" % request.form['username']
            result = db.query_db(query)

            if result==None :
                return render_template("login.html", error = "Nome utente o password errata")

            elif request.form['password']==result[0][1] :
                session['user_id'] = result[0][2]
                session['user_type'] = result[0][3]
                return redirect(url_for('route_home'))

            else:
                return render_template("login.html", error = "Nome utente o password errata")
        else:
            return render_template("login.html", logged=False)
    return redirect(url_for('route_home'))
