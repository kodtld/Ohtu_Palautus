from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoslista = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self.ostoslista:
            maara += ostos.lukumaara()
        
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for ostos in self.ostoslista:
            summa += ostos.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        ostosnimet = [ostos.tuotteen_nimi() for ostos in self.ostoslista]
        if Ostos(lisattava).tuotteen_nimi() not in ostosnimet:
            self.ostoslista.append(Ostos(lisattava))
        else:
            for ostos in self.ostoslista:
                if ostos.tuotteen_nimi() == Ostos(lisattava).tuotteen_nimi():
                    ostos.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostoslista:
            if ostos.tuotteen_nimi() == Ostos(poistettava).tuotteen_nimi():
                ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        self.ostoslista = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoslista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
