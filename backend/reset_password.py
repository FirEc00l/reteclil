'''
recovery.py
@author: Nicholas Sollazzo,Alesandro Capici
@version: 1.0
@date: 15/05/17
'''
from flask import request, render_template, abort
from flask import url_for
from flask import redirect
from werkzeug.security import generate_password_hash, \
     check_password_hash
import backend.clil_utils.db as utils

def reset_password(request,session,key):

    print 'yolo'

    if 'user_id' in session:
        abort(403)
    else:
        logged = True
    if key is not None:
            db = utils.pysqlite3()
            query = """SELECT key
                        FROM user
                        WHERE username="%s"
                        """ % user
            result=db.query_db(query)
            if result[0][0]==key:
                NewPassword=request.form['NewPassword']
                print NewPassword
                return redirect(url_for('route_home'))
    else:
        return redirect(url_for('route_reset_password'))

##    if condition:
##        return render_template("reset_password.html", logged=logged)
##    else:
##        return redirect(url_for('route_home'))
##
##    if request.method != 'POST':
##        NewPassword=request.form['NewPassword']
##        print NewPassword
##        return redirect('home.html',logged=logged)
##
##    else:
##        return redirect('home.html',logged=logged)

##            creazione nuova psw
##            onetimePSW = ''.join(random.choice('0123456789ABCDEF') for i in range(5))
##            ConetimePSW = onetimePSW
##            print ConetimePSW
##            #inserimento password db
##            onetimePSW=generate_password_hash(onetimePSW)
##            query = """UPDATE User
##                       SET password="%s"
##                       WHERE username="%s"
##                            """ % (onetimePSW,user)
##            db.query_db(query)
##
##            if request.method=='POST' :#modificare richiesta html
##                query = """SELECT username, password, id_user, user_type
##                           FROM User
##                           WHERE User.username="%s\"""" % username
##                result = db.query_db(query)
##
##                if check_password_hash(result[0][1],ConetimePSW):
##                    session['user_id'] = result[0][2]
##                    session['user_type'] = result[0][3]
##                    return redirect(url_for('account.html'),logged=logged,psw=ConetimePSW)
