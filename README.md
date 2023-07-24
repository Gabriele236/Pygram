# Pygram
README - Progetto InstaFace

Introduzione:

Il progetto "InstaFace" è una piattaforma social di base creata con Python che consente agli utenti di registrarsi, accedere, inviare amicizie, pubblicare post, comunicare tramite messaggi, e visualizzare i post dei propri amici. Il progetto utilizza il concetto di classi e oggetti per gestire gli utenti e i loro amici.

Requisiti:

Per eseguire il progetto, assicurati di avere Python installato sul tuo sistema. Inoltre, le librerie pandas e csv devono essere installate. Puoi installarle utilizzando i comandi:

bash
Copy code
pip install pandas
pip install csv
Struttura del Progetto:

Il progetto è costituito dai seguenti file:

main.py: Contiene il codice principale del progetto, inclusa la gestione dell'interazione con l'utente, la creazione di account, l'accesso, l'invio di richieste di amicizia, l'aggiunta di post e la gestione dei messaggi.

Classi.py: Contiene la definizione delle classi User e Friend utilizzate per rappresentare gli utenti e i loro amici. Queste classi contengono metodi per gestire le operazioni degli utenti.

Utenti.csv: Un file CSV contenente i dati degli utenti registrati, come nome, cognome, età, città, username e password.

Post.csv: Un file CSV contenente i dati dei post, come l'ID del post, l'utente che ha pubblicato il post, il tempo di pubblicazione e il contenuto del post.

Istruzioni:

Esegui il file main.py per avviare l'applicazione InstaFace.

Se sei un nuovo utente, rispondi "no" alla domanda "Hai già un account?" e segui le istruzioni per registrarti fornendo il tuo nome, cognome, età, città, username e password.

Se sei un utente registrato, rispondi "si" alla domanda "Hai già un account?" e inserisci il tuo username e la tua password per accedere.

Una volta effettuato l'accesso, puoi utilizzare il menu per selezionare le diverse azioni disponibili. Puoi visualizzare le notifiche, creare un nuovo post, visualizzare la tua pagina personale, visualizzare i post dei tuoi amici tramite la dashboard, inviare richieste di amicizia, accettare richieste di amicizia, inviare messaggi ai tuoi amici e altro ancora.

Quando hai finito, digita "logout" per uscire dall'applicazione.

Note:

Questo progetto è una versione di base di una piattaforma social e può essere ulteriormente esteso e migliorato per includere più funzionalità e un'interfaccia utente più sofisticata. Inoltre, è importante notare che questo progetto è solo a scopo educativo e potrebbe non essere adatto per un utilizzo reale su una piattaforma social completa.
