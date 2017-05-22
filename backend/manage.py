'''
manage.py
@author: Nicholas Sollazzo
@version: 1.3.3
@date: 22/05/17
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

import backend.clil_utils.db as utils
from backend.clil_utils.pyJson import pyJson as pj

from flask import request
from flask import render_template
from flask import abort

import os
import string

# Costants
DATA = pj('data/data.json')

# global
RESULT = 'Success'

def manage(request, session):

	DB =  utils.pysqlite3()

	def initResult():
		global RESULT
		if RESULT != 'Success':
			RESULT = 'Success'
		print 'RESULT:', RESULT

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
	        'create_user': create_user, # TBT
			'delete_user': delete_user, # TBT
	        'edit_description': edit_description, # DONE
			'update_user_password': update_user_password, # TBT
			'create_link': create_link, # DONE
			'delete_link': delete_link, # DONE
			'create_section': create_section,
			'delete_section': delete_section,
			'change_section': change_section,
			'rename_file': rename_file,
			'delete_file': delete_file
	    }
		initResult()
		funAction = switcher[requestAction]
		funAction()

	# XXX: 1
	def create_user():
		name = request.form['name']
		surname = request.form['surname']
		password = request.form['password']
		user_type = request.form['user_type']
		email = request.form['email']
		username = request.form['username']
		in_use = False

		query = ''' SELECT username FROM user; '''

		username_in_use = DB.query_db(query)

		for item in username_in_use:
			if item == username:
				in_use = True

		if in_use:
				setResult('username_already_in_use') # TODO implementare in manage.html, cambiare con numeri
		else:
			query = '''INSERT INTO user
			VALUES(NULL, "{name}", "{surname}", "{password}", "{user_type}", "{email}", "{username}", NULL);
			'''.format(name, surname, password, user_type, email, username)

			DB.query_db(query)
			DB.close_db()

			setResult('user_created') # TODO implementare in manage.html, cambiare con numeri

	# XXX: 2
	def delete_user():

		username = request.form['username']

		query = ''' DELETE user WHERE username = "{}"; '''.format(username)

		DB.query_db(query)
		DB.close_db()

		setResult('user_deleted') # TODO implementare in manage.html, cambiare con numeri

	# XXX: 3
	def edit_description():
		DATA.edit('description', request.form['new_description'])
		setResult('file_edited') # TODO implementare in manage.html, cambiare con numeri

	# XXX: 4
	def update_user_password():
		new_password = request.form['new_password']
		username = request.form['username']

		query = '''UPDATE user
				   SET password = "{0}"
				   WHERE username = "{1}";'''.format(new_password, username)

		setResult('password_updated') # TODO implementare in manage.html, cambiare con numeri

	# XXX: 5
	def create_link():
		title = request.form['link_title']
		url = request.form['link_url']

		in_use = False

		for link in DATA.read('links'):
			if title in link.values():
				in_use = True

		if not in_use:
			new_link = {'title' : title, 'url' : url}
			DATA.add('links', new_link)
		else:
			setResult('title_already_in_use') # TODO implementare in manage.html, cambiare con numeri

	# XXX: 6
	def delete_link():
		title = request.form['title']
		DATA.remove('links',title)

	# XXX: 7
	def create_section():
		pass

	# XXX: 8
	def delete_section():
		pass

	# XXX: 9
	def change_section():
		pass

	# XXX: 10
	def rename_file():
		pass

	# XXX: 11
	def delete_file():
		pass

	query = '''
            SELECT id_user
            FROM user;
            '''

	user_list = DB.query_db(query)
	print 'user_list:', user_list

	user_list_dict = []
	for user in user_list:

		print 'user', user

		query = '''
		SELECT name, surname, username, user_type
		FROM user
		WHERE id_user="{}";
		'''.format( str(user[0]) )
		result = DB.query_db(query)

		print 'result', result

		user_list_dict.append( {'name':result[0][0],
								'surname':result[0][1],
								'username':result[0][2],
								'user_type':result[0][3]} )

	user_list = user_list_dict

	print user_list

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
		print('NONE')

	section_list = []
	description = None

	if 'user_id' in session:
		logged = session['user_type']
		if logged != 3:
			abort(403)
	else:
		abort(403)

	links = DATA.read('links')
	description = DATA.read('description')

	if request.method != 'POST':

		DB.close_db()

		return render_template('manage.html', user_list=user_list, file_list=file_list, section_list=section_list,
								description=description, links=links, logged=logged) #Passare lista utenti e file da DB
	else:

		# print 'requestForm:', request.form
		getAction(request.form['action'])

		DB.close_db()

		return getResult()
