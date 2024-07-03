import datetime
from dataclasses import dataclass


@dataclass
class VotoDto:  # le entità della tabella devono essere associate ad un oggetto
    nome: str   # l'oggetto deve avere un attributo per ogni dato, ogni colonna
    CFU: int
    punteggio: int
    lode: bool
    data: datetime.date

    def __str__(self):
        return f"{self.nome} - CFU: {self.CFU} - punteggio: {self.punteggio} "

    def __eq__(self, other):  # due entità della tabella sono uguali quando le loro chiavi primarie sono uguali
        return self.nome == other.nome  # perché la chiave primaria è il nome

    def __hash__(self):  # stessa cosa, basato solo sulla chiave primaria, se avessi altri attributi, foreign keys,
        return hash(self.nome)  # potrei fare hash di una tupla, di più cose
