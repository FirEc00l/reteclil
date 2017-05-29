import pyMail

link = 'http://www.repubblica.it/tecnologia/sicurezza/2017/05/18/news/adylkuzz_il_virus_piu_intelligente_di_wannacry-165758066/'

msg = "Rete CLIL della provincia di Pavia\nE' stato effettuato un tentativo di recupero della password per il tuo account della Rete CLIL della provincia di Pavia\nPer recuperare la password premi qui\n{}\nIn alternativa, copia questo link nella barra degli indirizzi\n{}".format(
    link, link)

pyMail.mail('reteclilpavia@gmail.com', 'robot1ca', 'sollsharp@gmail.com',
            'prova', msg, '../../templates/Mail.html', 'placeholder', link)
