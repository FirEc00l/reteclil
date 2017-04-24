'''
manage.py
@author: Nicholas Sollazzo
@version: 0.0
@date: 10/04/17
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

from flask import request, render_template

def manage(request):
	if request.method == 'POST':
		return render_template('manage.html',)

	else:
                user_list = []
                file_list = []
                section_list = []
		return render_template('manage.html', user_list=user_list, file_list=file_list, section_list=section_list)
