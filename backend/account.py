##devo contrallare se è presente la sessione (se sono loggato) controllare se il tipo è post
##


#from flask import Flask
from flask import render_tempalte
#app=flask(__name__)
#@app.route('/')

def account(request, session):
    if 'user_id' in session:
        if request.method=='POST' :
            db = pysqlite3()
            query = """SELECT User.email
                        FROM User
                        WERE 
                        """
        else:
            return render_template("acoount.html",email=)
            
            
            
        
