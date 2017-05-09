from flask import render_template, url_for, redirect

def logout(session):
    # remove the username from the session if it's there
    if 'user_id' in session:
        session.pop('user_id', None)
        session.pop('user_type', None)
        return redirect(url_for('route_home'))
    else:
        return redirect(url_for('route_home'))
