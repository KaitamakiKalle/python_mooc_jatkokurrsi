# TEE RATKAISUSI TÄHÄN:
class Suorakulmio:
    def __init__(self, leveys: int, korkeus: int):
        self.leveys = leveys
        self.korkeus = korkeus

    def __str__(self):
        return f"suorakulmio {self.leveys}x{self.korkeus}"

    def pinta_ala(self):
        return self.leveys * self.korkeus


class Nelio(Suorakulmio):

    def __init__(self, sivu: int):
        super().__init__(sivu, sivu)

    def __str__(self):
        return f'neliö {self.leveys}x{self.korkeus}'
