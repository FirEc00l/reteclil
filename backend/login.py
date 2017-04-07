#from flask import Flask, request, render_template
#app = Flask(__name__)

#@app.route("/login", methods=['GET', 'POST'])

def login():
    if 'user_id' not in session:
        if methods=='POST' :
            session['user_id'] = 1 
    return redirect(url_for('home'))
