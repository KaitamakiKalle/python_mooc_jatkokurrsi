# TEE RATKAISUSI TÄHÄN:
class Alkio:
    """ Luokka mallintaa yhtä alkiota binääripuussa """

    def __init__(self, arvo, vasen_lapsi: 'Alkio' = None, oikea_lapsi: 'Alkio' = None):
        self.arvo = arvo
        self.vasen_lapsi = vasen_lapsi
        self.oikea_lapsi = oikea_lapsi


def suurin_alkio(juuri: 'Alkio'):
    suurin = juuri.arvo

    if juuri.oikea_lapsi is not None:

        oikea = suurin_alkio(juuri.oikea_lapsi)
        if oikea > suurin:
            suurin = oikea

    if juuri.vasen_lapsi is not None:
        vasen = suurin_alkio(juuri.vasen_lapsi)
        if vasen > suurin:
            suurin = vasen

    return suurin
