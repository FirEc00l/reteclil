#sstampa tutti i post della discussione
#se conne ssione epost inserisci post
'''
thread.py
@author:Alesandro Capici
@version: 0.1
@date: 26/05/17
'''
from flask import render_template, abort ,request, redirect , url_for
import backend.clil_utils.db as utils


def thread (request, session, id_thread):
    if 'user_id' in session:
        logged = session['user_type']
        if request.method=='POST':
            print 'nico'
            testo=request.form['textarea1']
            print 'yolo',testo
            return render_template("thread.html")
     
        else:
            db =  utils.pysqlite3()
            query = """SELECT title
                       FROM thread
                       WHERE  id_thread = '%s'
                        """ %  id_thread
            result = db.query_db(query)
            titolo=result[0][0]

            query = """ SELECT post.*,user.username
                        FROM post
                        NATURAL JOIN user
                        WHERE id_thread = '%s'
                        """ % id_thread
            result = db.query_db(query)
            post=result


            dict_files = []
            extension = []
            print 'ciao'
            for posts in post:
                dict_files.append({'id': posts[0], 'text': posts[1], 'author': posts[6], 'date': posts[3]})
                
            print dict_files
            return render_template("thread.html",thread_title=titolo, id=id_thread,  logged=logged,post=dict_files)
    else :
        abort(403)




