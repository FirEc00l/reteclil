'''
manage.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.5.3
@date: 6/06/17
===============================================
manage(request):
renderizzare il template manage.html
		oppure
processare la richiesta di aggiornamento dati:
    *Creazione user
    *Eliminazione user
    *Eliminazione file
    *Aggiornare descrizione
    *Generare password utente
    *Creare link
    *Eliminare link
    *Creare nuova sezione
    *Eliminare una sezione vuota
    *Cambiare la sezione di un file
    *Rinominare un file
================================================
'''

import os
import string

from flask import abort, render_template, request
from werkzeug.security import generate_password_hash

import backend.clil_utils.db as utils
import backend.clil_utils.pyMail as pm
import backend.clil_utils.pyUser as pyu
from backend.clil_utils.pyJson import pyJson as pj

# Costants
DATA = pj('data/data.json')
CLIL_MAIL = 'reteclilpavia@gmail.com'
CLIL_MAIL_PSW = 'robot1ca'
# global
RESULT = 'Success'


def manage(request, session):

    DB = utils.pysqlite3()

    def initResult():
        global RESULT
        if RESULT != 'Success':
            RESULT = 'Success'

    def setResult(new_result):
        global RESULT
        if RESULT == 'Success':
            RESULT = new_result
        return RESULT

    def getResult():
        global RESULT
        return RESULT

    def getAction(requestAction):
        # print 'requestAction:', requestAction
        switcher = {
            'edit_description': edit_description,  # 1 DONE
            'create_link': create_link,  # 2 DONE
            'delete_link': delete_link,  # 3 DONE
            'create_user': create_user,  # 4 DONE
            'delete_user': delete_user,  # 5 DONE
            'create_section': create_section,  # 6 TBT
            'delete_section': delete_section,  # 7 TBT
            'create_sub_section': create_sub_section,  # 8 DEV
            'delete_sub_section': delete_sub_section,  # 9 TBT
            'change_file_section': change_file_section,  # 10 TBT
            'delete_file': delete_file  # 11 TBT
        }
        initResult()
        funAction = switcher[requestAction]
        funAction()

    # XXX: 1
    def edit_description():
        DATA.edit('description', request.form['new_description'])

    # XXX: 2
    def create_link():
        title = request.form['link_title']
        url = request.form['link_url']

        in_use = False

        for link in DATA.read('links'):
            if title in link.values():
                in_use = True

        if not in_use:
            new_link = {'title': title, 'url': url}
            DATA.add('links', new_link)
        else:
            setResult('title_already_in_use')

    # XXX: 3
    def delete_link():
        title = request.form['title']
        DATA.remove('links', title)

    # XXX: 4
    def delete_user():
        username = request.form['username']

        query = ''' SELECT id_user
					FROM user
					WHERE username = "{}"; '''.format(username)

        id_to_be_deleted = DB.query_db(query)

        if id_to_be_deleted == session['user_id']:
            # TODO implementare in manage.html, cambiare con numeri
            setResult('Error')
        else:
            query = '''DELETE FROM user
					   WHERE username = "{}";'''.format(username)

            DB.query_db(query)
            DB.close_db()

    # XXX: 5
    def create_user():
        name = request.form['name']
        surname = request.form['surname']
        password = pyu.pswgen('0123456789ABCDEF', 5)
        user_type = request.form['user_type']
        email = request.form['email']
        username = pyu.usrgen(name.lower(), surname.lower())
        in_use = False

        query = ''' SELECT email FROM user; '''

        email_in_use = DB.query_db(query)

        for item in email_in_use:
            if item == email:
                in_use = True
                break

        if in_use:
            # TODO implementare in manage.html, cambiare con numeri
            setResult('email_already_in_use')
        else:
            query = '''INSERT INTO user
					   VALUES(NULL, "{}", "{}", "{}", "{}", "{}", "{}", NULL);
						'''.format(name, surname, generate_password_hash(password), user_type, email, username)

            DB.query_db(query)
            DB.close_db()

            email_subject = 'Registrazione rete CLIL pavia'
            email_body = "Ben Venuto nella rete clil di pavia!\nIl tuo username e': {}\nla tua password e': {}\nVI preghiamo di cambiare la password al primo accesso".format(
                username, password)

            pm.send_email(CLIL_MAIL, CLIL_MAIL_PSW, email,
                          email_subject, email_body)

    # XXX: 6
    def create_section():
        section_name = request.form['section_name']
        in_use = False

        query = ''' SELECT section_name FROM section; '''

        section_name_in_use = DB.query_db(query)

        for item in section_name_in_use:
            if item == section_name:
                in_use = True
                break

        if in_use:
            setResult('section_name_already_in_use')
        else:
            query = '''INSERT INTO section
					   VALUES(NULL, "{}");
					'''.format(section_name)

            DB.query_db(query)
            DB.close_db()

    # XXX: 7
    def delete_section():
        id_section = request.form['id_section']

        query = '''SELECT COUNT(id_sub)
				   FROM sub_section
				   WHERE id_section = "{}"; '''.format(id_section)

        subs = int(DB.query_db(query)[0][0])

        if subs > 0:
            setResult('subs')
        else:
            query = '''DELETE FROM section WHERE id_section = "{}"; '''.format(
                id_section)

            DB.query_db(query)
            DB.close_db()

    # XXX: 8
    def create_sub_section():
        sub_section_name = request.form['sub_section_name']
        id_section = request.form['id_section']

        query = '''SELECT COUNT(id_sub)
			       FROM sub_section
			       WHERE sub_name = "{}";'''.format(sub_section_name)

        sub_name = int(DB.query_db(query)[0][0])

        if sub_name > 0:
            setResult('name')
        else:
            query = '''INSERT INTO sub_section
					   VALUES (NULL, "{}", "{}");'''.format(sub_section_name, id_section)

            DB.query_db(query)
            DB.close_db()

    # XXX: 8
    def delete_sub_section():
        sub_section_id = request.form['sub_section_id']

        query = '''SELECT COUNT(id_file)
				   FROM file
				   WHERE id_sub = "{}"; '''.format(sub_section_id)

        files = int(DB.query_db(query)[0][0])

        if files > 0:
            setResult('files')
        else:
            query = '''DELETE FROM sub_section
					   WHERE id_sub = "{}"; '''.format(sub_section_id)

        DB.query_db(query)
        DB.close_db()

    # XXX: 9
    def change_file_section():
        id_file = request.form['id_file']
        new_id_sub = request.form['new_id_sub']

        query = '''UPDATE file
				   SET id_sub = "{}"
				   WHERE id_file = "{}";'''.format(new_id_sub, id_file)

        DB.query_db(query)
        DB.close_db()

    # XXX: 10
    def delete_file():
        id_file = request.form['id_file']

        query = ''' SELECT name
				 	FROM file
					WHERE id_file = "{}"; '''.format(id_file)

        path = 'static/' + DB.query_db(query)[0][0]

        print path

        query = ''' DELETE FROM file
				 	WHERE id_file = "{}"; '''.format(id_file)

        DB.query_db(query)

        os.remove(path)

        DB.close_db()

    # XXX: 0
    query = '''
            SELECT id_user
            FROM user;
            '''

    user_list = DB.query_db(query)

    user_list_dict = []
    for user in user_list:

        query = '''SELECT name, surname, username,email, user_type
				   FROM user
				   WHERE id_user="{}";'''.format(str(user[0]))
        result = DB.query_db(query)

        user_list_dict.append({'name': result[0][0],
                               'surname': result[0][1],
                               'username': result[0][2],
                               'email': result[0][3],
                               'user_type': result[0][4]})

    user_list = user_list_dict

    if user_list is None:
        user_list = []
        print 'Query returned no result'

    query = '''
            SELECT *
            FROM file;
            '''

    file_list = DB.query_db(query)

    if file_list is not None:
        file_list = list(file_list)
    else:
        file_list = []
        print 'file_list: Query returned no result'

    if file_list is None:
        print 'NONE'

    section_list = []
    description = None

    if 'user_id' in session:
        logged = session['user_type']
        if logged != 3:
            abort(403)
    else:
        abort(403)

    query = '''SELECT section_name, id_section
			   FROM section;'''
    sections = DB.query_db(query)

    for section in sections:
        query = '''SELECT sub_name, id_sub
				   FROM sub_section
				   WHERE id_section="{}"; '''.format(str(section[1]))
        result = DB.query_db(query)
        section_list.append(
            {'name': section[0], 'list': result, 'id_section': section[1]})

    links = DATA.read('links')
    description = DATA.read('description')

    if request.method != 'POST':

        DB.close_db()

        return render_template('manage.html', user_list=user_list, file_list=file_list, section_list=section_list,
                               description=description, links=links, logged=logged)  # Passare lista utenti e file da DB
    else:

        # print 'requestForm:', request.form
        getAction(request.form['action'])

        DB.close_db()

        return getResult()
