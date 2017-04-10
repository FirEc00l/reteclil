#from flask import Flask
from flask import render_template, url_for, redirect
#app = Flask(__name__)

#@app.route("/login", methods=['GET', 'POST'])

def login(request, session):

    if 'user_id' not in session:
        
        if request.method=='POST' :
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            
            db =  pysqlite3()
            query = """SELECT User.username User.password
                       FROM User
                       WHERE User.username=%s""" % session['username']
            result = db.query_db(query)
            
            if(result==None):
                print "login fallito, l'utente non esiste"
                
            else if(session['password']==result[0][1]):
                print "login effettuato"
                return redirect(url_for('home'))
            
            else:
                print "login fallito, password errata"
        else:
            return render_template("login.html")
    return redirect(url_for('home'))
