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
                Form_hash_psw=generate_password_hash(request.form['oldpassword'])
                if check_password_hash(password,Form_hash_psw):
                    newPassword=request.form['newpassword']
                    newPassword=generate_password_hash(newPassword)
                    query = """UPDATE User
                        SET password="%s"
                        WHERE id_user=%s
                        """ % (newPassword, session['user_id'])
                    db.query_db(query)
                    return render_template("account.html",email=mail,success="modifica effettuata", logged=logged)
                else:
                    return render_template("account.html",email=mail,error="Password errata", logged=logged)
            if request.form['action']=='email':
                Form_hash_psw=generate_password_hash(request.form['password'])
                if check_password_hash(password,Form_hash_psw):
                    newMail=request.form['newemail']
                    query = """UPDATE User
                        SET email="%s"
                        WHERE User.id_user=%s
                        """ % (newMail, session['user_id'])
                    db.query_db(query)
                    return render_template("account.html",email=newMail,success="modifica effettuata", logged=logged)
                else:
                   return render_template("account.html",email=mail,error="Password errata", logged=logged)
        else:
            return render_template("account.html",email=mail, logged=logged)


    else:
        abort(403)
