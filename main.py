from Classi import User
import pandas as pd
import csv
from Classi import Friend

entry = False
username = ""
password = ""
check = True
check_psw = True

#LEGGI I FILE CSV
Utenti_csv = "Utenti.csv"
name_columns = ["new_id", "nome", "cognome", "età", "città", "username", "password"]
df = pd.read_csv(Utenti_csv, names=name_columns)
Post_csv = "Post.csv"
post_columns = ["new_id","poster","time","post"]
df_post = pd.read_csv(Post_csv, names=post_columns)


def welcome_message():
    print("Benvenuto su InstaFace!\nTi trovi sulla nuova piattaforma Social totalmente made in Italy\n")


def message_error():
    print("ERRORE\nAzione non eseguibile")


def add_friend(current_user, receiver):
    for friend in current_user.friend_list:
        if receiver.username == friend.username:
            receiver.add_notice(f"Nuova richiesta di amicizia da {current_user.username}")
            receiver.add_friend_request(current_user)
            print("Richiesta inviata")
            break
    else:
        print("Contatto non trovato")


def check_password(password):
    special_sym = ["$", "@", "#", "%"]
    psw_accepted = True
    if len(password) < 8:
        print("La password deve contenere almeno 8 caratteri")
        psw_accepted = False
    if not any(char.isdigit() for char in password):
        print("La password deve contenere almeno un numero")
        psw_accepted = False
    if not any(char.isupper() for char in password):
        print("La password deve contenere almeno una lettera maiuscola")
        psw_accepted = False
    if not any(char.islower() for char in password):
        print("La password deve contenere almeno una lettera minuscola")
        psw_accepted = False
    if not any(char in special_sym for char in password):
        print(f"La password deve contenere almeno un carattere speciale {special_sym}")
        psw_accepted = False

    return psw_accepted


def get_last_id(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            last_id = 0
            for row in reader:
                if row:  # Assicurati che ci siano elementi nella riga
                    last_id = int(row[0])
            return last_id
    except FileNotFoundError:
        return 0


def check_username(username):
    col_username = df[df.columns[5]]
    for i in col_username:
        if i == username:
            return True  # Username già esiste, quindi restituisci True
    return False  # Nessun username corrispondente, quindi restituisci False



def check_age(age):
    if age < 18:
        print("Hai meno di 18 anni")
        return False
    return True


def check_log_in(username, password):
    if password != User.all_user.get(username):
        print("Password errata")
        return False
    return True

def verifica_credenziali(username, password):
    # Trova l'indice della riga corrispondente all'username
    username_index = df[df['username'] == username].index

    # Verifica se l'username è presente nel DataFrame
    if not username_index.empty:
        # L'username è presente, ora controlla la password solo nella riga corrispondente
        row = df.loc[username_index[0]]
        if row['password'] == password:
            return False
        else:
            return True
    else:
        # L'username non è presente nel DataFrame
        return True


def stampa_post_amico(amico):
    friend_rows = df_post[df_post['poster'] == amico]
    if not friend_rows.empty:
        print(f"Post di {amico}:")
        for _, row in friend_rows.iterrows():
            print(f"Tempo: {row['time']}")
            print(f"Messaggio: {row['post']}")
            print()
    else:
        print(f"{amico} non ha pubblicato nessun post.")








#SCHERMATA INZIALE: ACCEDI O REGISTRATI
welcome_message()  # stampa un messaggio di benvenuto "Benvenuto su InstaFace!"
first_choice = input("Hai già un account? [si] [no]").lower()
if first_choice != "si" and first_choice != "sì":
    name = input("Inserisci il tuo nome: \n")
    surname = input("Inserisci il tuo cognome: \n")
    age = int(input("Inserisci la tua età: \n"))
    city = input("Inserisci la tua città: \n")
    while True:
        username = input("Inserisci un username: \n")
        if not check_username(username):  # Utilizza il valore restituito dalla funzione per interrompere il ciclo
            break
        else:
            print("Username già utilizzato,prova altro")

    while True:
        password = input("Inserisci una password: \n")
        if check_password(password):  # Utilizza il valore restituito dalla funzione per interrompere il ciclo
            break
    # Ottieni l'ultimo ID e incrementalo
    last_id = get_last_id("Utenti.csv")
    new_id = last_id + 1
    # Scrivi i dati nel file CSV
    with open("Utenti.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([new_id, name, surname, age, city,username,password])
    print("I tuoi dati sono stati registrati. Riavvia l'applicazione prima di fare login")


# FASE DI LOGIN
while entry is False:
    print("Log in\n")
    username = input("Inserisci il tuo username: \n")
    password = input("Inserisci una password: \n")
    if verifica_credenziali(username, password):
        print("Password o username sbagliati")
    else:
        entry = True
        print(f"Benvenuto di nuovo {username}")
        break



#CREAZIONE OGGETTO UTENTE
username_index = df[df['username'] == username].index
row = df.loc[username_index[0]]
nome_utente = row['nome']
cognome_utente = row['cognome']
età_utente = row['età']
città_utente = row['città']
password_utente = row['password']
Current_User = User(nome_utente,cognome_utente,username,password,città_utente,età_utente)
Current_User.friend_list_request.append("Cipollino97") #aggiungiamo un utente di default che fa una richiesta di amicizia


# INIZIO CORE DEL PROGRAMMA
id_choice = False
while id_choice is False:
    menu_choice = input("""Scegli un'azione dal menu\nMenu: \n\
        1- Visualizza le notifiche\n\
        2- Crea un nuovo post\n\
        3- Visualizza Pagina Personale\n\
        4- Visualizza Dashboard\n\
        5- Manda una richiesta di amicizia\n\
        6- Accetta una richiesta di amicizia\n\
        7- Apri una chat\n\
        8- Fai un upgrade a premium (NON ANCORA DISPONIBILE)\n\
        9- Vedi i tuoi amici\n\
        10- Imposta Privacy (NON ANCORA DISPONIBILE)\n\
        Digita logout per uscire da InstaFace\n\
        """)
    # MOSTRA NOTIFICHE
    if menu_choice == "1":
        Current_User.show_notice()

    # AGGIUNGI POST
    elif menu_choice == "2":
        Current_User.add_post()



    #visualizza pagina personale
    elif menu_choice == "3":
        Current_User.show_homepage()



    #visualizza Dashboard DA FARE
    elif menu_choice == "4":
        for amico in Current_User.friend_list:
            stampa_post_amico(amico)


    # manda una richiesta di amicizia
    elif menu_choice == "5":
        request_choice = input("A chi vuoi inviare una richiesta di amicizia?")
        if check_username(request_choice):
            username_index = df[df['username'] == request_choice].index
            row = df.loc[username_index[0]]
            nome_friend = row['nome']
            cognome_friend = row['cognome']
            età_friend = row['età']
            città_friend = row['città']
            password_friend = row['password']
            username_friend = row['username']
            friend = Friend(nome_utente, cognome_utente, username_friend, password_friend, città_utente, età_utente)
            friend.friend_list_request.append(username)
            print(f"Richiesta inviata a {request_choice}. Aspettiamo con calma")
        else:
            print("Oops, Utente non trovato")

    # accetta una richiesta di amicizia
    elif menu_choice == "6":
        print("Hai le seguenti richieste di amicizia:")
        for request in Current_User.friend_list_request:
            choice = input(f"Accettare richiesta da {request} [si] [no]")
            if choice.lower() == "si" or "sì":
                Current_User.friend_list.append(request)
                print(f"Hai aggiunto {request} ai tuoi amici, ora puoi mandarli un messaggio e visitare la sua bacheca")
                Current_User.friend_list_request.remove(request)
            elif choice.lower() == "no":
                Current_User.friend_list_request.remove(request)
            else:
                print("OOPS, qualcosa è andato storto")

    # manda un messaggio a un tuo amicone
    elif menu_choice == "7":
        receiver = input("A chi vuoi scrivere un messaggio")
        content = input("Cosa vuoi scrivere?")
        if receiver in Current_User.friend_list:
            Current_User.add_message(receiver,content)
            Current_User.show_inbox()
            username_index = df[df['username'] == receiver].index
            row = df.loc[username_index[0]]
            nome_friend  = row['nome']
            cognome_friend = row['cognome']
            età_friend = row['età']
            città_friend = row['città']
            password_friend = row['password']
            username_friend = row['username']
            friend = Friend(nome_utente, cognome_utente, username_friend, password_friend, città_utente, età_utente)
            friend.receive_message(username,content)
        else:
            print("Utente non trovato: l'utente non esiste oppure non è tuo amico")

    #VEDI LISTA AMICI
    elif menu_choice == "9" :
        Current_User.show_friendlist()

    #IMPOSTAZIONI PRIVACY
    elif menu_choice =="10":
        pass

    # LOGOUT
    elif menu_choice.lower() == "logout":
        print("A presto!")
        break



