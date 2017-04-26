'''
manage.py
@author: Nicholas Sollazzo
@version: 0.4
@date: 26/04/17
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

from flask import request
from flask import render_template
import json
import os

def manage(request):

	def action():
	    switcher = {
	        'create_user': create_user(),
			'delete_user': delete_user(),
	        'delete_file': delete_file(),
	        'edit_description': edit_description(),
			'update_user_password': update_user_password(),
			'create_link': create_link(),
			'delete_link': delete_link(),
			'create_section': create_section(),
			'delete_section': delete_section(),
			'change_section': change_section(),
			'rename_file': rename_file()
	    }
	    return switcher.get(action, 'error')

	def create_user(arg):
		pass

	def delete_user(arg):
		pass

	def delete_file(arg):
		pass

	def edit_description(new_description):
		with open('data/data.json', 'r') as f:
		    json_data = json.load(f)
		    json_data[description] = new_description

		with open('data/data_tmp.json', 'w') as f: # temporary json with new changes
			f.write(json.dumps(json_data))

		os.rename('data/data_tmp.json', 'data/data.json') # rename the temporary file onto the original file
		pass

	def update_user_password(arg):
		pass

	def create_link(arg):
		pass

	def delete_link(arg):
		pass

	def create_section(arg):
		pass

	def delete_section(arg):
		pass

	def change_section(arg):
		pass

	def rename_file(arg):
		pass

	if request.method == 'POST':
		return render_template('manage.html',)

	else:
		user_list = []
		file_list = []
		section_list = []

		action(request.form[action])

		#passare sempre links e description

		with open('data/data.json') as data_file:
			data_str = data_file.read()
			links = json.loads(data_str)['links']
			description = json.loads(data_str)['description']

		return render_template('manage.html', user_list=user_list, file_list=file_list, section_list=section_list,
								description=description, links=links)
