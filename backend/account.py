from flask import render_template
import backend.clil_utils.db as utils


def account(request, session):
    db = utils.pysqlite3()
    if 'user_id' in session:
        query = """SELECT password
                        FROM User
                        WHERE id_user=%s
                        """ % session['user_id']
        result=db.query_db(query)
        password=result[0][0]
        
        query = """SELECT email
                        FROM User
                        WHERE id_user=%s
                        """ % session['user_id']
        result=db.query_db(query)
        mail=result[0][0]

        if request.method=='POST' :
            if request.form['action']=='password':
                if password==request.form['oldpassword']:
                    newPassword=request.form['newpassword']
                    query = """UPDATE User
                        SET password="%s"
                        WHERE id_user=%s
                        """ % (newPassword, session['user_id'])
                    db.query_db(query)
                    return render_template("account.html",email=mail)
                else:
                    return render_template("account.html",email=mail,error="Password errata")
            if request.form['action']=='email':
                if password==request.form['password']:
                    newMail=request.form['newemail']
                    query = """UPDATE User
                        SET email="%s"
                        WHERE User.id_user=%s
                        """ % (newMail, session['user_id'])
                    db.query_db(query)
                    return render_template("account.html",email=mail)
                else:
                   return render_template("account.html",email=mail,error="Password errata")
        else:
            return render_template("account.html",email=mail)
            
    
    else:
    	query = """SELECT email
                        FROM User
                        WHERE id_user=%s
                        """ % session['user_id']
        result=db.query_db(query)
        mail=result[0][0]
        return render_template("account.html",email=mail)
       
