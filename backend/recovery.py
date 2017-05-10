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
import backend.clil_utils.db as utils
import random

def recovery(request,session):
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
        
        #creazione nuova psw
        onetimePSW = ''.join(random.choice('0123456789ABCDEF') for i in range(5))
        
        SendMail = 'reteclilpavia@gmail.com' 
        password = 'robot1ca'

##        # Open a plain text file for reading.  For this example, assume that
##        # the text file contains only ASCII characters.
##        fp = open(textfile, 'rb')"noreply@reteclil.it"
##        # Create a text/plain message
##        msg = MIMEText(fp.read())
##        fp.close()
        
        #formattazzione messaggio
        FormatoMessaggio = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s"
        msg= "La tua  nuova password Provvisoria e' : "+ onetimePSW
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
        
        #inserimento password db
        onetimePSW=generate_password_hash(onetimePSW)
        query = """UPDATE User
                        SET password="%s"
                        WHERE username="%s"
                        """ % (onetimePSW,user)
        db.query_db(query)
        return render_template("recovery.html",success="modifica effettuata",logged=logged)
        
