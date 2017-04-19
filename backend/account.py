
##devo contrallare se è presente la sessione (se sono loggato) controllare se il tipo è post
##se non è post reindirizzo il template con parametro email
##se prendoi 


#from flask import Flask
from flask import render_tempalte
#app=flask(__name__)
#@app.route('/')

def account(request, session):
    db = pysqlite3()
    if 'user_id' in session:
        if request.method=='POST' :
            if request.action=='password':
                query = """SELECT password
                        FROM User
                        WHERE id_user=%s
                        """ % session['user_id']
                result=db.query_db(query)
                password=result[0][4]
                if password==request.form['oldpassword']:
                    newPassword=request.form['newpassword']
                    query = """UPDATE User
                        SET password=%s
                        WHERE id_user=%s
                        """ % newPassword, session['user_id']
                else:
                    #errore
            if request.action=='email':
                query = """SELECT email
                        FROM User
                        WHERE id_user=%s
                        """ % session['user_id']
                result=db.query_db(query)
                mail=result[0][6]
                if mail==request.form['oldemail']:
                    newMail=request.form['newemail']
                    query = """UPDATE User
                        SET email=%s
                        WHERE User.id_user=%s
                        """ % newMail, session['user_id']
                else:
                    ##errore
                    
                
        else:
            query = """SELECT email
                        FROM User
                        WHERE id_user=%s
                        """ % session['user_id']
            result=db.query_db(query)
            mail=result[0][6]
            return render_template("acoount.html",email=mail)
            
            
            
        
