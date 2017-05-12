'''
account.py
@author: Alesandro Capici
@date: 8/5/17
'''
from flask import render_template, abort
import backend.clil_utils.db as utils
from werkzeug.security import generate_password_hash, \
     check_password_hash


def account(request, session):
    db = utils.pysqlite3()
    if 'user_id' in session:
        logged = session['user_type']
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
                if check_password_hash(password,request.form['oldpassword']):
                    newPassword=request.form['newpassword']
                    newPassword=generate_password_hash(newPassword)
                    query = """UPDATE User
                        SET password="%s"
                        WHERE id_user=%s
                        """ % (newPassword, session['user_id'])
                    db.query_db(query)
                    return render_template("account.html",email=mail,success="modifica effettuata", logged=logged)
                else:
                    return render_template("account.html",email=mail,error="Password errata", errorType="password", logged=logged)
            if request.form['action']=='email':
                if check_password_hash(password,request.form['password']):
                    newMail=request.form['newemail']
                    query = """UPDATE User
                        SET email="%s"
                        WHERE User.id_user=%s
                        """ % (newMail, session['user_id'])
                    db.query_db(query)
                    return render_template("account.html",email=newMail,success="modifica effettuata", logged=logged)
                else:
                   return render_template("account.html",email=mail,error="Password errata", errorType="email", logged=logged)
        else:
            return render_template("account.html",email=mail, logged=logged)


    else:
        abort(403)
