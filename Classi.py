from datetime import datetime
import csv

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

class User:

    def __init__(self, name, surname, username, password, city, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.username = username
        self.password = password
        self.friend_list = []
        self.friend_list_request = []
        self.inbox = []
        self.notice = [] # Initialize the notice attribute as an empty list
        self.homepage = []



    def show_inbox(self):
        if self.inbox:
            print("Messaggi nell'inbox di", self.username)
            for msg in self.inbox:
                print(msg)
        else:
            print("La tua inbox è vuota")

    def add_message(self,receiver,content):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.inbox.append({"Messaggio da": self.name,
                           "A:" : receiver,
                              "Time": time,
                              "Contenuto": content})


    def show_notice(self):
        print(self.notice)

    def add_post(self):
        poster = self.username
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        post = input("Scrivi qualcosa: esprimiti liberamente...ma non troppo:")
        self.homepage.append({"Published by":poster,
                              "Time":time,
                              "Content of":post})
        # Ottieni l'ultimo ID e incrementalo
        last_id = get_last_id("Utenti.csv")
        new_id = last_id + 1
        # Scrivi i dati nel file CSV
        with open("Post.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_id, poster, time, post])
        print("Post pubblicato, visita la homepage per vederlo")



    def add_friend_request(self,friend):
        Friend.friend_list_request.append(friend)
        print(f"Hai aggiunto {friend} ai tuoi amici, ora puoi mandarli un messaggio e visitare la sua bacheca")


    def show_friendlist(self):
        print(self.friend_list)


    def show_friendlist_request(self):
        print(self.friend_list_request)

    def show_homepage(self):
        print(self.homepage)



class Friend(User):
    def __init__(self, name, surname, username, password, city, age):
        super().__init__(name, surname, username, password, city, age)

    def receive_message(self, sender, content):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.inbox.append({
            "Messaggio da": sender,
            "A:": self.username,
            "Time": time,
            "Contenuto": content
        })
        self.notice.append(f"Messaggio ricevuto da {sender}")




