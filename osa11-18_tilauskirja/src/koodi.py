# Tee ratkaisusi tähän:

class Tehtava:
    id_laskija = 0

    def __init__(self, kuvaus: str, koodari: str, tyomaara: int):
        self.__id = Tehtava.id_laskija
        Tehtava.id_laskija += 1
        self.__kuvaus = kuvaus
        self.__koodari = koodari
        self.__tyomaara = tyomaara
        self.__valmis = False

    @property
    def id(self):
        return self.__id

    @property
    def kuvaus(self):
        return self.__kuvaus

    @property
    def koodari(self):
        return self.__koodari

    @property
    def tyomaara(self):
        return self.__tyomaara

    def on_valmis(self):
        return self.__valmis

    def merkkaa_valmiiksi(self):
        self.__valmis = True

    def __str__(self):
        return f'{self.__id}: {self.__kuvaus} ({self.__tyomaara} tuntia), koodari {self.__koodari} {"VALMIS" if self.__valmis else "EI VALMIS"}'


class Tilauskirja:

    def __init__(self):
        self.__tilaukset = {}
        self.__koodarit = []

    def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):
        id = Tehtava.id_laskija
        self.__tilaukset[id] = Tehtava(
            kuvaus, koodari, tyomaara)

        self.__koodarit.append(koodari)
        self.__koodarit = list(set(self.__koodarit))

    def kaikki_tilaukset(self):
        return list(self.__tilaukset.values())

    def koodarit(self):
        return self.__koodarit

    def merkkaa_valmiiksi(self, id: int):
        if id not in self.__tilaukset:
            raise ValueError()
        tilaus = self.__tilaukset[id]
        tilaus.merkkaa_valmiiksi()

    def valmiit_tilaukset(self):
        return [self.__tilaukset[tehtava] for tehtava in self.__tilaukset if self.__tilaukset[tehtava].on_valmis()]

    def ei_valmiit_tilaukset(self):
        return [self.__tilaukset[tehtava] for tehtava in self.__tilaukset if not self.__tilaukset[tehtava].on_valmis()]

    def koodarin_status(self, koodari: str):
        if koodari not in self.__koodarit:
            raise ValueError()

        valmiit = 0
        ei_valmiit = 0
        valmiit_tyoaika = 0
        ei_valmiit_tyoaika = 0
        for i in self.__tilaukset:
            tehtava = self.__tilaukset[i]
            if tehtava.koodari != koodari:
                continue
            else:
                if tehtava.on_valmis():
                    valmiit += 1
                    valmiit_tyoaika += tehtava.tyomaara
                else:
                    ei_valmiit += 1
                    ei_valmiit_tyoaika += tehtava.tyomaara
        return (valmiit, ei_valmiit, valmiit_tyoaika, ei_valmiit_tyoaika)
