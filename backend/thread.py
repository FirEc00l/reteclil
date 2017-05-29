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
        if request.method=='POST' :
            abort(403)
        else:
            db =  utils.pysqlite3()
            query = """SELECT title
                       FROM thread
                       WHERE  id_thread = '%s'
                        """ %  id_thread
            result = db.query_db(query)
            titolo=result[0][0]

            query = """ SELECT *
                        FROM post
                        WHERE id_thread = '%s'
                        """ % id_thread
            result = db.query_db(query)
            post=result

            dict_files = []
            extension = []
            for post in post:
                id_post = post[0]
                content = post[1]
                date_post = post[2]
                id_user = post[3]
                dict_files.append({'post_id': post[0], 'post.text': post[1], 'post.data': post[2], 'post.author': post[3]})
                
            return render_template("forum.html",thread_title=titolo,  logged=logged,post=dict_files)
    else :
        abort(403)




