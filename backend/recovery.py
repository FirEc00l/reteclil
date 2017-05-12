'''
recovery.py
@author: Nicholas Sollazzo,Alesandro Capici,Cristian Garau
@version: 1.4
@date: 10/05/17
@note: testato ma non funzionante
'''

from flask import request, render_template, abort
from werkzeug.security import generate_password_hash, \
     check_password_hash
from email.mime.text import MIMEText as mt
# Import smtplib for the actual sending function
import smtplib
import time
import backend.clil_utils.db as utils
import random

def recovery(request,session,key=None):
    if 'user_id' in session:
        abort(403)
    else:
        logged = False
    if request.method != 'POST':
        print 'key2:',key
        if key is not None:
            query = """SELECT key
                        FROM user
                        WHERE username="%s"
                        """ % user
            result=db.query_db(query)
            if result[0][0]==key:
                return render_template("reset_password.html", logged=logged)
        else:
            return render_template("recovery.html",logged=logged)
    else:
        db = utils.pysqlite3()
        user = request.form['user']
        query = """SELECT email
                        FROM user
                        WHERE username="%s"
                        """ % user
        result=db.query_db(query)
        ReciveMail=result[0][0]
        data=time.strftime("%H:%M:%S")
        rand=''.join(random.choice('0123456789ABCDEF') for i in range(5))
        MailHash=ReciveMail+data+rand
        MailHash=generate_password_hash(ReciveMail)



        link='http://127.0.0.1:5000/recovery/'+ MailHash
        SendMail = 'reteclilpavia@gmail.com'
        password = 'robot1ca'


        #formattazzione messaggio
        FormatoMessaggio = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s"
        msg= "E' stata ricevuta una richiesta di reimpostazione password, per cambiarla accedere al link seguente : "+ link
        Oggetto="Recupero password"
        messaggio = FormatoMessaggio%(SendMail, ReciveMail, Oggetto, msg)

        '''
        fp = open(textfile, 'rb')
        html = fp.read()
        part1 = MIMEText(messaggio, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)

        '''

        #invio mail con nuova password
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(SendMail,password)
        s.sendmail(SendMail,ReciveMail,messaggio)
        #s.sendmail(SendMail,ReciveMail,msg.as_string())
        s.quit()

        query = """UPDATE User
                   SET key="%s"
                   WHERE username="%s"
                            """ % (MailHash,user)
        db.query_db(query)

        print 'key:',key


##            #creazione nuova psw
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


        return render_template("recovery.html",success="modifica effettuata",logged=logged)
