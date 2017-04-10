import clil_utils.db
from flask import render_template, url_for, redirect
#app = Flask(__name__)

#@app.route("/login", methods=['GET', 'POST'])

def account(request, session):

    if 'user_id' in session:

        
        if request.method=='POST' :
		 db =  pysqlite3()
            	 query = """SELECT User.email
                       FROM User
                       WHERE """
            	 result = db.query_db(query)
	else :
		return redirect(url_for('account.html',email=))
            
