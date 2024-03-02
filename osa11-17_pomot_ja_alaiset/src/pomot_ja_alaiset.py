# TEE RATKAISUSI TÄHÄN:
class Tyontekija:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.alaiset = []

    def lisaa_alainen(self, tyontekija: 'Tyontekija'):
        self.alaiset.append(tyontekija)


def laske_alaiset(tyontekija: 'Tyontekija'):
    summa = len(tyontekija.alaiset)

    if summa == 0:
        return 0

    for i in tyontekija.alaiset:
        summa += laske_alaiset(i)
    return summa
