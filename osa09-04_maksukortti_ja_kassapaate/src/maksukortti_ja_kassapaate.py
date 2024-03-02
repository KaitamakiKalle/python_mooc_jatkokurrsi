# TEE RATKAISUSI TÄHÄN:

class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays

    def ota_rahaa(self, maara: float):
        # Toteuta metodi siten, että se ottaa kortilta rahaa vain, jos saldoa riittää
        # Onnistuessaan metodi palauttaa True ja muuten False
        if self.saldo >= maara:
            self.saldo -= maara
            return True
        else:
            return False


class Kassapaate:
    def __init__(self):
        # kassassa on aluksi 1000 euroa rahaa
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti(self, maksu: float):
        # Edullinen lounas maksaa 2.50 euroa
        # Kasvatetaan kassan rahamäärää edullisen lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
        hinta = 2.5
        if maksu >= hinta:
            self.rahaa += maksu
            self.edulliset += 1
            self.rahaa -= maksu - hinta
            return maksu - hinta
        else:
            return maksu

    def syo_maukkaasti(self, maksu: float):
        # Maukas lounas maksaa 4.30 euroa
        # Kasvatetaan kassan rahamäärää maukkaan lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
        hinta = 4.3
        if maksu >= hinta:
            self.rahaa += maksu
            self.maukkaat += 1
            self.rahaa -= maksu - hinta
            return maksu - hinta
        else:
            return maksu

    def syo_edullisesti_kortilla(self, kortti: Maksukortti):
        # Edullinen lounas maksaa 2.50 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False
        hinta = 2.5
        if kortti.saldo >= hinta:
            kortti.ota_rahaa(hinta)
            self.rahaa += hinta
            self.edulliset += 1

    def syo_maukkaasti_kortilla(self, kortti: Maksukortti):
        # Maukas lounas maksaa 4.30 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False
        hinta = 4.3
        if kortti.saldo >= hinta:
            kortti.ota_rahaa(hinta)
            self.rahaa += hinta
            self.maukkaat += 1

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):
        self.rahaa += summa
        kortti.lataa_rahaa(summa)
