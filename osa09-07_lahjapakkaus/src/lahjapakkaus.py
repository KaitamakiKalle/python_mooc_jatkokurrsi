# TEE RATKAISUSI TÄHÄN:
class Lahja:

    def __init__(self, nimi: str, paino: int):
        self.nimi = nimi
        self.paino = paino


class Pakkaus:

    def __init__(self):
        self.lahjat = []
        self.yhtpaino = 0

    def lisaa_lahja(self, lahja: 'Lahja'):
        self.lahjat.append(lahja)
        self.yhtpaino += lahja.paino

    def yhteispaino(self):
        return self.yhtpaino
