'''
recovery.py
@author: Nicholas Sollazzo,Alesandro Capici,Cristian Garau
@version: 1.0
@date: 3/05/17
@note: testato ma non funzionante
'''

from flask import request, render_template, abort
from werkzeug.security import generate_password_hash, \
     check_password_hash
from email.mime.text import MIMEText as mt
# Import smtplib for the actual sending function
import smtplib
import request
import backend.clil_utils.db as utils
import random

def recovery(request,session,key=None):
    if 'user_id' in session:
        abort(403)
    else:
        logged = False
    if request.method != 'POST':
        return render_template('recovery.html', logged=logged)
    else:
        db = utils.pysqlite3()
        user = request.form['user']
        query = """SELECT email
                        FROM user
                        WHERE username="%s"
                        """ % user
        result=db.query_db(query)
        ReciveMail=result[0][0]
        MailHash=generate_password_hash(ReciveMail)
        
        
        
        link='http://127.0.0.1:5000/account/'+ MailHash
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
        
        if key is not None:
            query = """SELECT username
                        FROM user
                        WHERE key="%s"
                        """ % MailHash
            result=db.query_db(query)
            username=result[0][0]
            
            #creazione nuova psw
            onetimePSW = ''.join(random.choice('0123456789ABCDEF') for i in range(5))
            
            #inserimento password db
            onetimePSW=generate_password_hash(onetimePSW)
            query = """UPDATE User
                       SET password="%s"
                       WHERE username="%s"
                            """ % (onetimePSW,user)
            db.query_db(query)

            if request.method=='POST' :#modificare richiesta html
                db =  utils.pysqlite3()
                query = """SELECT username, password, id_user, user_type
                           FROM User
                           WHERE User.username="%s\"""" % request.form['username']
                result = db.query_db(query)
                if result==None :
                    return render_template("login.html", error = "Nome utente o password errata", logged=False)
            
                elif check_password_hash(result[0][1],request.form['password']):
                    session['user_id'] = result[0][2]
                    session['user_type'] = result[0][3]
                    return redirect(url_for('route_home'))

                else:
                    return render_template("login.html", error = "Nome utente o password errata", logged=False)
        
        else:
            return render_template("recovery.html",logged=logged)
            
            
        return render_template("recovery.html",success="modifica effettuata",logged=logged)
        
