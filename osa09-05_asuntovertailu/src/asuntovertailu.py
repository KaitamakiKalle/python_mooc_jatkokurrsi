# TEE RATKAISUSI TÄHÄN:

class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta

    def suurempi(self, asunto: 'Asunto'):
        return True if self.nelioita > asunto.nelioita else False

    def hintaero(self, verrattava: 'Asunto'):
        return abs(self.neliohinta * self.nelioita - verrattava.neliohinta * verrattava.nelioita)

    def kalliimpi(self, verrattava: 'Asunto'):
        return True if self.neliohinta * self.nelioita > verrattava.neliohinta * verrattava.nelioita else False
