# Tee ratkaisusi tähän:

class Sarja:

    def __init__(self, nimi: str, kaudet: int, genret: list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.genret = genret
        self.arvostelut = []

    def __str__(self):
        return f'{self.nimi} ({self.kaudet} esityskautta)\ngenret: {", ".join(self.genret)}\n{"ei arvosteluja" if len(self.arvostelut) == 0 else f"arvosteluja {len(self.arvostelut)}, keskiarvo {round(sum(self.arvostelut)/len(self.arvostelut), 1)} pistettä"}'

    def arvostele(self, arvosana: int):
        if arvosana >= 0 & arvosana <= 5:
            self.arvostelut.append(arvosana)


def arvosana_vahintaan(arvosana: float, sarjat: list):
    valitut = []
    for i in sarjat:
        if round(sum(i.arvostelut)/len(i.arvostelut), 1) > arvosana:
            valitut.append(i)

    return valitut


def sisaltaa_genren(genre: str, sarjat: list):
    valitut = []
    for i in sarjat:
        if genre in i.genret:
            valitut.append(i)
    return valitut
