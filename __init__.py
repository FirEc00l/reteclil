'''
__init__.py
@author: Nicholas Sollazz
@version: 1.0
@date: 3/04/17
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    # lista di stringhe contenente i nomi delle sezioni
    sections

    # True se è presente una sessione
    # False se non è presente una sessione
    logged #boolean

    # nome utente dell’utente loggato [se presente in sessione]
    username
    pass

@app.route("/section/<section>")
def section(section):
    pass

@app.route("/login")
def login(request):
    pass

@app.route("/recovery")
def recovery(request):
    pass

@app.route("/upload")
def upload(request):
    pass

@app.route("/account")
def account(request):
    # email dell’user corrente
    email
    pass

@app.route("/manage")
def manage(request):
    pass

@app.route("/logout")
def logout(request):
    pass

@app.route("/forum")
def forum(requst):
    # lista dei thread, ogni thread ha titolo (title) e autore (author)
    thread_list
    pass

@app.route("/forum/<thread_id>")
def thread(request):
    # titolo thread
    title

    # lista dei post associati al thread, ogni post ha data (date), titolo (title) e testo(text)
    post_list
    pass

@app.route("/search/<search_key>")
def search(request):
    # chiave di ricerca
    search_key
    pass

if __name__ == "__main__":
    app.run()
