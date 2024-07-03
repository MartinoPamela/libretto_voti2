import mysql.connector
import pathlib   # mi permette di trovare il file di configurazione in modo programmatico


class DBConnect:
    def __init__(self):
        pass

    def get_connection(self):  # metodo che funziona come una factory di connessioni
        # factory è un pattern di programmazione che in qualche modo implementa le funzioni che generano oggetti
        # quindi incapsula il costruttore di un metodo e restituiscono un oggetto, un'istanza di una classe
        # in questo caso ci restituisce un oggetto mysql connection
        try:
            # cnx = mysql.connector.connect(user='root', password='pami', host='127.0.0.1', database='libretto')
            # cnx = mysql.connector.connect(option_files="./database/config.cnf")  questo è il percorso relativo al main
            cnx = mysql.connector.connect(option_files=f"{pathlib.Path(__file__).resolve().parent}/config.cnf")
            # in questo modo ho il path assoluto
            return cnx
        except mysql.connector.Error as err:
            print(err)
            return None


