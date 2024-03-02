# TEE RATKAISUSI TÄHÄN:
class SuperSankari:
    def __init__(self, nimi: str, supervoimat: str):
        self.nimi = nimi
        self.supervoimat = supervoimat

    def __str__(self):
        return f'{self.nimi}, superkyvyt: {self.supervoimat}'


class SuperRyhma():

    def __init__(self, nimi: str, kotipaikka: str):
        self._nimi = nimi
        self._kotipaikka = kotipaikka
        self._jasenet = []

    @property
    def nimi(self):
        return self._nimi

    @property
    def kotipaikka(self):
        return self._kotipaikka

    def lisaa_jasen(self, sankari: 'SuperSankari'):
        self._jasenet.append(sankari)

    def tulosta_ryhma(self):
        print(f'{self._nimi}, {self._kotipaikka}')
        print('Jäsenet:')
        for i in self._jasenet:
            print(f'{i.nimi}, superkyvyt: {i.supervoimat}')
