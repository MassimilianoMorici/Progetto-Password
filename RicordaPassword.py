
import pyperclip
import json

# Leggi il file JSON esistente (se esiste) per inizializzare il dizionario psw
try:
    with open('passwords.json', 'r') as json_file:
        psw = json.load(json_file)
except FileNotFoundError:
    psw = {}


while True:
    scelta = input(
        '\nCosa vuoi fare? (digita il numero)\n\n1) per aggiungere un sito \n2) per cercare una password \n3) per eliminare un sito e password \n4) per uscire \n\n--> ')

    # aggiungi
    if scelta == '1':
        nuovoSitoPsw = {}
        aggiungiSito = input('\nNome del sito: ').lower()
        aggiungiPsw = input('\nAggiungi password: ')
        nuovoSitoPsw[aggiungiSito] = aggiungiPsw
        psw.update(nuovoSitoPsw)

        # Salva il dizionario psw nel file JSON
        with open('passwords.json', 'w') as json_file:
            json.dump(psw, json_file)

    # ottieni password
    elif scelta == '2':
        print('\nSiti registrati:\n')
        for sito in psw:
            print('- '+sito)
        sitoScelto = input(
            "\nInserisci il nome del sito per ottenere la password corrispondente (o '3' per uscire): ").lower()

        if sitoScelto == '4':
            break

        try:
            passwordScelta = psw[sitoScelto]
            pyperclip.copy(passwordScelta)
            print('\nPassword trovata! Ora puoi incollarla\n')
        except KeyError:
            print('\nPassword non trovata! Riprova\n')

    # elimina
    elif scelta == '3':
        print('\nSiti registrati:\n')
        for sito in psw:
            print('- '+sito)
        eliminaSito = input(
            '\nInserisci il nome del sito da eliminare: ').lower()
        if eliminaSito in psw:
            del psw[eliminaSito]
            print(f'\nIl sito "{eliminaSito}" è stato eliminato.\n')

            # Salva il dizionario psw nel file JSON dopo la rimozione
            with open('passwords.json', 'w') as json_file:
                json.dump(psw, json_file)
        else:
            print(f'\nIl sito "{eliminaSito}" non è stato trovato!\n')

    # esci
    elif scelta == '4':
        break
    else:
        print('\nScelta non valida. Riprova.')
