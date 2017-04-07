from flask import render_template, url_for, redirect

#@app.route('/logout')

def logout():
    # remove the username from the session if it's there
    session.pop('user_id', None)
    return redirect(url_for('home'))
