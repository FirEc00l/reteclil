##            creazione nuova psw
##            onetimePSW = ''.join(random.choice('0123456789ABCDEF') for i in range(5))
##            ConetimePSW = onetimePSW
##            print ConetimePSW
##            #inserimento password db
##            onetimePSW=generate_password_hash(onetimePSW)
##            query = """UPDATE User
##                       SET password="%s"
##                       WHERE username="%s"
##                            """ % (onetimePSW,user)
##            db.query_db(query)
##
##            if request.method=='POST' :#modificare richiesta html
##                query = """SELECT username, password, id_user, user_type
##                           FROM User
##                           WHERE User.username="%s\"""" % username
##                result = db.query_db(query)
##
##                if check_password_hash(result[0][1],ConetimePSW):
##                    session['user_id'] = result[0][2]
##                    session['user_type'] = result[0][3]
##                    return redirect(url_for('account.html'),logged=logged,psw=ConetimePSW)
