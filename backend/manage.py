'''
manage.py
@author: Nicholas Sollazzo
@version: 0.1.1
@date: 2/05/17
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

from flask import request
from flask import render_template
from flask import abort

import json
import os
import string

def manage(request, session):

	def getAction(requestAction):
		switcher = {
	        'create_user': create_user,
			'delete_user': delete_user,
	        'delete_file': delete_file,
	        'edit_description': edit_description, #WORKING!
			'update_user_password': update_user_password,
			'create_link': create_link,
			'delete_link': delete_link,
			'create_section': create_section,
			'delete_section': delete_section,
			'change_section': change_section,
			'rename_file': rename_file
	    }

		funAction = switcher[requestAction]
		funAction()

	def create_user():
		pass

	def delete_user():
		pass

	def delete_file():
		pass

	def edit_description():
		new_description = request.form['new_description']
		with open('data/data.json', 'r') as f:
			json_data = json.load(f)
			json_data['description'] = new_description

		with open('data/data_tmp.json', 'w') as f: # temporary json with new changes
			f.write(json.dumps(json_data))

		os.remove('data/data.json')
		os.rename('data/data_tmp.json', 'data/data.json') # rename the temporary file onto the original file

	def update_user_password():
		pass

	def create_link():

		pass

	def delete_link():
		pass

	def create_section():
		pass

	def delete_section():
		pass

	def change_section():
		pass

	def rename_file():
		pass

	db =  utils.pysqlite3()

	query = '''
            SELECT *
            FROM user
            '''

	user_list = db.query_db(query)

	if user_list is not None:
		user_list = list(user_list)
	else:
		user_list = []
		print 'Query returned no result'

	user_list = list( db.query_db(query) )

	query = '''
            SELECT *
            FROM file
            '''

	file_list = db.query_db(query)

	if file_list is not None:
		file_list = list(file_list)
	else:
		file_list = []
		print 'Query returned no result'

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

	if request.method != 'POST':

		with open('data/data.json') as data_file:
			data_str = data_file.read()
			links = json.loads(data_str)['links']
			description = json.loads(data_str)['description']

		return render_template('manage.html', user_list=user_list, file_list=file_list, section_list=section_list,
								description=description, links=links, logged=logged) #Passare lista utenti e file da DB
	else:

		getAction(request.form['action'])

		with open('data/data.json') as data_file:
			data_str = data_file.read()
			links = json.loads(data_str)['links']
			description = json.loads(data_str)['description']

		return render_template('manage.html', user_list=user_list, file_list=file_list, section_list=section_list,
								description=description, links=links, logged=logged)
