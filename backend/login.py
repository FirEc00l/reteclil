#from flask import Flask
from flask import render_template, url_for, redirect
#app = Flask(__name__)

#@app.route("/login", methods=['GET', 'POST'])

def login(request, session):

    if 'user_id' not in session:
        
        if request.method=='POST' :
            
            
            db =  pysqlite3()
            query = """SELECT User.username User.password User.id_user
                       FROM User
                       WHERE User.username=%s""" % request.form['username']
            result = db.query_db(query)
            
            if result==None :
                print "login fallito, l'utente non esiste"
                
            elif request.form['password']==result[0][1] :
                print "login effettuato"
                session['user_id'] = result[0][2]
                return redirect(url_for('home'))
            
            else:
                print "login fallito, password errata"
        else:
            return render_template("login.html")
    return redirect(url_for('home'))
