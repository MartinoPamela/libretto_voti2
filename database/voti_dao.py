import mysql.connector
from modello.voto_dto import VotoDto
from database.db_connect import DBConnect


class VotiDao:

    def __init__(self):
        self.db_connect = DBConnect()  # lo inizializzo una volta, lo creo quest'oggetto

    def get_voti(self):  # questo metodo non ha parametri perché devo semplicemente leggere tutti i voti,
        # se devo inserire un nuovo voto probabilmente avrò bisogno di un metodo con i parametri dove specifico il voto

        cnx = self.db_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                FROM voti"""

        cursor.execute(query)
        # print(cursor.fetchall())  # questo metodo mi stampa i voti, insieme all'if == 'main'
        # faccio un test per vedere che tutto funzioni
        result = []
        for row in cursor:
            result.append(VotoDto(row["nome"],
                                  row["cfu"],
                                  row["punteggio"],
                                  bool(row["lode"]),
                                  row["data"]))
        cursor.close()
        cnx.close()
        return result  # prima chiudere le risorse poi fare return
        # qualcosa deve restituire

    def add_voti(self, voto: VotoDto) -> None:  # è un int che do all'editor in modo che l'editor mi possa aiutare
        # facendo l'autocompletamento
        # mi aspetto che mi passa un oggetto, quindi un voto

        cnx = self.db_connect.get_connection()
        if cnx is None:
            print("Errore")
            return
        cursor = cnx.cursor(dictionary=True)
        query = """
        INSERT INTO voti
        (nome, cfu, punteggio, lode, data)
        VALUES (%s, %s, %s, %s, %s)"""

        cursor.execute(query, (voto.nome, voto.CFU, voto.punteggio, voto.lode, voto.data))
        cnx.commit()
        cursor.close()
        cnx.close()
        # in questo caso il return non mi serve, quindi lo tolgo anche dall'except


if __name__ == '__main__':  # questo metodo è un test per vedere che tutto funzioni,senza non mi stamperebbe il fetchall
    voti_dao = VotiDao()    # mi stampa una lista di esami con il fetchall
    voti_dao.get_voti()
