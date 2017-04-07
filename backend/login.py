#from flask import Flask, request, render_template
#app = Flask(__name__)

#@app.route("/login", methods=['GET', 'POST'])

def login(request, session):
    if 'user_id' not in session:
        if request.method=='POST' :
            session['user_id'] = 1 
    return redirect(url_for('home'))
