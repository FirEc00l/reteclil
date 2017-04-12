
##devo contrallare se è presente la sessione (se sono loggato) controllare se il tipo è post
##se non è post reindirizzo il template con parametro email
##se prendoi 


#from flask import Flask
from flask import render_tempalte
#app=flask(__name__)
#@app.route('/')

def account(request, session):
    if 'user_id' in session:
        if request.method=='POST' :
            
            
        else:
            db = pysqlite3()
            query = """SELECT User.email
                        FROM User
                        WHERE User.id_user=%s
                        """ % session['user_id']
            result=db.query_db(query)
            mail=result[0][6]
            return render_template("acoount.html",email=mail)
            
            
            
        
