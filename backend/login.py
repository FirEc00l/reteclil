#controllare se la richiesta � post, se lo � fare login 
#altrimenti renderizzare il template login.html

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/login")

def login():
    if methods=='POST' :
        #garau deve fare il login in sql ciao
       
    else :
         return render_template("login.html")
