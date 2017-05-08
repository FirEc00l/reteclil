'''
recovery.py
@author: Nicholas Sollazzo,Alesandro Capici
@version: 1.0
@date: 3/05/17
@note: non testato
'''

from flask import request, render_template, abort

# Import smtplib for the actual sending function
import smtplib
import backend.clil_utils.db as utils
# Import the email modules we'll need
from email.mime.text import MIMEText as mt

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
                        WHERE "username"=%s
                        """ % user
        result=db.query_db(query)
        ReciveMail=result[0][0]
        onetimePSW = ''.join(random.choice('0123456789ABCDEF') for i in range(5))

        '''
        @TODO: messaggino carino
        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        fp = open(textfile, 'rb')"noreply@reteclil.it"
        # Create a text/plain message
        msg = MIMEText(fp.read())
        fp.close()
        '''
        SendMail = "noreply@reteclil.it"

        msg = mt('La tua nuova password e\':' + onetimePSW)
        
        msg['Subject'] = 'Recupero password'
        msg['From'] = SendMail
        msg['To'] = ReciveMail

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.sendmail(SendMail, ReciveMail, msg.as_string())
        s.quit()
