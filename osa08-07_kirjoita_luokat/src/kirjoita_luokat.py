# Tee ratkaisusi tähän:
# Luokka Muistilista
# attribuutti otsikko (merkkijono)
# attribuutti merkinnat (lista)

class Muistilista:

    def __init__(self, otsikko: str, merkinnat: list):
        self.otsikko = otsikko
        self.merkinnat = merkinnat

# Luokka Asiakas
# attribuutti tunniste (merkkijono)
# attribuutti saldo (desimaaliluku)
# attribuutti alennusprosentti (kokonaisluku)


class Asiakas:

    def __init__(self, tunniste: str, saldo: float, alennusprosentti: int):
        self.tunniste = tunniste
        self.saldo = saldo
        self.alennusprosentti = alennusprosentti

# Luokka Kaapeli
# attribuutti malli (merkkijono)
# attribuutti pituus (desimaaliluku)
# attribuutti maksiminopeus (kokonaisluku)
# attribuutti kaksisuuntainen (totuusarvo)


class Kaapeli:

    def __init__(self, malli: str, pituus: float, maksiminopeus: int, kaksisuuntainen: bool):
        self.malli = malli
        self.pituus = pituus
        self.maksiminopeus = maksiminopeus
        self.kaksisuuntainen = kaksisuuntainen
