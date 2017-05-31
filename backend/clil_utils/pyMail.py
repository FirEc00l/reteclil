'''
pyMail.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.0
@date: 31/05/17
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(from_gmail, from_gmail_psw, to_email, subject, body, html_path=None, placeholder=None, link=None):

    # formattazzione messaggio
    mime_msg = MIMEMultipart('alternative')
    mime_msg['Subject'] = subject
    mime_msg['From'] = from_gmail
    mime_msg['To'] = to_email

    part1 = MIMEText(body, 'plain')
    mime_msg.attach(part1)

    if html_path is not None:
        with open(html_path, 'rb') as fp:
            html_part = fp.read()
        part2 = MIMEText(html_part, 'html')
        mime_msg.attach(part2)

    # invio mail con link
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(from_gmail, from_gmail_psw)
    # s.sendmail(SendMail,ReciveMail,messaggio)
    if placeholder is not None and link is not None:
        s.sendmail(from_gmail, to_email,
                   mime_msg.as_string().replace(placeholder, link))
    else:
        s.sendmail(from_gmail, to_email, mime_msg.as_string())
    s.quit()

    if s:
        return True
    else:
        return False
