# TEE RATKAISUSI TÄHÄN:

class Lottorivi:

    def __init__(self, kierros: int, luvut: list):
        self.kierros = kierros
        self.luvut = luvut

    def osumien_maara(self, oma_rivi: list):
        return len([luku for luku in oma_rivi if luku in self.luvut])

    def osumat_paikoillaan(self, pelattu_rivi: list):
        return [luku if luku in self.luvut and (pelattu_rivi.index(luku) == self.luvut.index(luku)) else -1 for luku in pelattu_rivi]
