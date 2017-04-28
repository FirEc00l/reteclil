'''
recovery.py
@author: Nicholas Sollazzo
@version: 0.9
@date: 7/04/17
@note: non testato
'''

from flask import request, render_template

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText as mt

import random

def recovery(request,session):

    if request.method != 'POST':
        return render_template('recovery.html')
    else:
        email = request.form['user']

        onetimePSW = ''.join(random.choice('0123456789ABCDEF') for i in range(5))

        '''
        @TODO: messaggino carino
        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        fp = open(textfile, 'rb')
        # Create a text/plain message
        msg = MIMEText(fp.read())
        fp.close()
        '''

        msg = mt('La tua nuova password e\':' + onetimePSW)

        me = 'noReply@reteclil.org' # the sender's email address

        msg['Subject'] = 'Recupero password'
        msg['From'] = me
        msg['To'] = email

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.sendmail(me, [email], msg.as_string())
        s.quit()
