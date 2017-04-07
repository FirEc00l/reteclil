#from flask import Flask
from flask import render_template, url_for, redirect
#app = Flask(__name__)

#@app.route("/login", methods=['GET', 'POST'])

def login(request, session):
    if 'user_id' not in session:
        if request.method=='POST' :
            session['user_id'] = 1
        else:
            return render_temeplate("login.html")
    return redirect(url_for('home'))
