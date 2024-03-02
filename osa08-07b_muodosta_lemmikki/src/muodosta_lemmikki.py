# Tee ratkaisusi tähän:

# Määrittele luokka Lemmikki. Luokalla on konstruktori, jossa annetaan arvot attribuuteille nimi, laji ja syntymavuosi tässä järjestyksessä.

# Kirjoita sitten luokan ulkopuolelle funktio uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int),
# joka luo ja palauttaa uuden Lemmikki-tyyppisen (eli Lemmikki-luokkaa vastaavan) olion.

class Lemmikki:

    def __init__(self, nimi: str, laji: str, syntymavuosi: int):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi


def uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int):

    return Lemmikki(nimi, laji, syntymavuosi)
