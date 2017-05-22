# -*- coding: cp1252 -*-
'''
recovery.py
@author: Nicholas Sollazzo,Alesandro Capici,Cristian Garau
@version: 1.8
@date: 19/05/17
@note: testato ma non funzionante
'''

from flask import request
from flask import render_template
from flask import abort
from flask import url_for
from flask import redirect
from werkzeug.security import generate_password_hash, \
     check_password_hash

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Import smtplib for the actual sending function
import smtplib
import time
import backend.clil_utils.db as utils
import random
#no post reindirizzo template se è e cambio psw             

def recovery(request,session, key=None):
    if 'user_id' in session:
        abort(403)
    else:
        logged = False    
    if request.method != 'POST':
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


        link='http://127.0.0.1:5000/reset_password/'+ MailHash
        SendMail = 'reteclilpavia@gmail.com'
        password = 'robot1ca'


        #formattazzione messaggio
        mime=MIMEMultipart('alternative')
        FormatoMessaggio = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s"
        msg= "E' stata ricevuta una richiesta di reimpostazione password, per cambiarla accedere al link seguente : "+ link
        Oggetto="Recupero password"
        messaggio = FormatoMessaggio%(SendMail, ReciveMail, Oggetto, msg)

        print link
        
        fp = open('templates/Mail.html', 'rb')
        html = fp.read()
        part1 = MIMEText(messaggio, 'plain')
        part2 = MIMEText(html, 'html')
        mime.attach(part1)
        mime.attach(part2)

        
        #invio mail con nuova password
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(SendMail,password)
        #s.sendmail(SendMail,ReciveMail,messaggio)
        s.sendmail(SendMail,ReciveMail,mime.as_string())
        s.quit()

        query = """UPDATE User
                   SET key="%s"
                   WHERE username="%s"
                            """ % (MailHash,user)
        db.query_db(query)
        return render_template("recovery.html",success="modifica effettuata",logged=logged)         
    
