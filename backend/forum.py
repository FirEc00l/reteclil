'''
forum.py
@author: Vincenzo Di Pietro
@date: 19/05/17
'''

import backend.clil_utils.db as utils
from flask import render_template, url_for, redirect
import datetime as dt
from datetime import datetime

def forum(request, session):

    if 'user_id' in session:
		logged = session['user_type']
    else:
        abort(403)

    db =  utils.pysqlite3()



    def print_threads():

        result_dict = []

        query = "SELECT id_thread, title, id_user, name, surname FROM thread NATURAL JOIN user"
        result = db.query_db(query)

        if result is None :
            threads = None
            return render_template("forum.html", logged=logged, threads=threads)

        else:
            for thread in result:
                            result_dict.append( {'id_thread': thread[0], 'title' : thread[1], 'id_user' : thread[2], 'name' : thread[3], 'surname' : thread[4]} )
            threads = result_dict

            print threads

            query = """SELECT count(id_thread) FROM thread WHERE id_user=%s""" %session['user_id']
            result = db.query_db(query)

            nthread = result[0][0] 

            print nthread

            return render_template("forum.html", logged=logged, threads=threads, nthread=nthread)


    if request.method=='POST' :

            if  request.form['request'] == "delete" :
                
                print "richiesta di delete ricevuta"

                query = """DELETE FROM thread
                       WHERE id_thread=\"{}\"""".format(request.form['id_thread'])

                result1 = db.query_db(query)

                print result1

                query = """DELETE FROM post
                       WHERE id_thread=\"{}\" """.format(request.form['id_thread'])
                
                result2 = db.query_db(query)

                print result2

                

                rt = print_threads()

                return rt
            
                
            else: 

                print "dati probabilmente ricevuti"

                date = dt.datetime.now()

                date = str(date.strftime("%d/%m/%y"))

                print "worka sempre di piu' ed oggi e' il: " + date

                print request.form['title'] + " " + request.form['content']
            
                query = """INSERT INTO thread
                       VALUES (NULL, \"{}\", \"{}\")""".format(request.form['title'], session['user_id'])

                result1 = db.query_db(query)

                print result1

                query = "SELECT id_thread FROM thread "

                result2 = db.query_db(query)
                
                id_trd = str(result2[-1][-1])

                print id_trd
                
                query = """INSERT INTO post
                       VALUES (NULL, \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")""".format(request.form['title'], request.form['content'], date, session['user_id'], id_trd)

                result3 = db.query_db(query)

                print result3

                return render_template("thread.html/"+id_trd)
            

    else:	

        rt = print_threads()

        return rt

    
    

'''

cueri   
        
        
'''
