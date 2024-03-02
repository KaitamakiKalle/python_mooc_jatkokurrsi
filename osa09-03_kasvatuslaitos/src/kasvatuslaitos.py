
# TEE RATKAISUSI TÄHÄN:
# Huom! Älä muuta luokkaa Henkilo!

class Henkilo:
    def __init__(self, nimi: str, ika: int, pituus: int, paino: int):
        self.nimi = nimi
        self.ika = ika
        self.pituus = pituus
        self.paino = paino


class Kasvatuslaitos:
    def __init__(self):
        self.punnitusten_lkm = 0

    def punnitse(self, henkilo: Henkilo):
        self.punnitusten_lkm += 1
        return henkilo.paino

    def syota(self, henkilo: Henkilo):
        henkilo.paino += 1
        return henkilo

    def punnitukset(self):
        return self.punnitusten_lkm
