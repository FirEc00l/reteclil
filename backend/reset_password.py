# -*- coding: cp1252 -*-
from flask import render_template
from flask import abort
from flask import url_for
from flask import redirect
from werkzeug.security import generate_password_hash, \
     check_password_hash
from email.mime.text import MIMEText as mt
# Import smtplib for the actual sending function
import smtplib
import time
import backend.clil_utils.db as utils
import random
#no post reindirizzo template se è e cambio psw


def reset_password(request,session, key=None):
    print 'garau'
    return redirect(url_for('route_reset_password'))
