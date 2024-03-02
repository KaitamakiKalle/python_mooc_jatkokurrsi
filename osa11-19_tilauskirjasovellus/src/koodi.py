# tee ratkaisusi tänne
# jos käytät edellisessä tehtävässä tekemiäsi luokkia, kopioi ne tänne
# Tee ratkaisusi tähän:

class Tehtava:
    id_laskija = 1

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
                    valmiit_tyoaika += int(tehtava.tyomaara)
                else:
                    ei_valmiit += 1
                    ei_valmiit_tyoaika += int(tehtava.tyomaara)
        return (valmiit, ei_valmiit, valmiit_tyoaika, ei_valmiit_tyoaika)


class Sovellus:

    def __init__(self):
        self.tilauskirja = Tilauskirja()

    def ohje(self):
        print('komennot:')
        print('0 lopetus')
        print('1 lisää tilaus')
        print("2 listaa valmiit")
        print("3 listaa ei valmiit")
        print("4 merkitse tehtävä valmiiksi")
        print("5 koodarit")
        print("6 koodarin status")

    def lisaa_tilaus(self):
        kuvaus = input('kuvaus:')
        koodari_tyomaara = input('koodari ja työmääräarvio:').split(' ')
        if len(koodari_tyomaara) < 2 or not koodari_tyomaara[1].isdigit():
            print('virheellinen syöte')
        else:
            self.tilauskirja.lisaa_tilaus(
                kuvaus, koodari_tyomaara[0], koodari_tyomaara[1])
            print('lisätty!')

    def valmiit(self):
        tehtavat = self.tilauskirja.valmiit_tilaukset()
        if len(tehtavat) == 0:
            print('ei valmiita')
        else:
            for i in tehtavat:
                print(i)

    def ei_valmiit(self):
        tehtavat = self.tilauskirja.ei_valmiit_tilaukset()
        if len(tehtavat) == 0:
            print('kaikki valmiita')
        else:
            for i in tehtavat:
                print(i)

    def merkitse_valmiiksi(self):
        tunniste = input('tunniste:')
        if not tunniste.isdigit() or int(tunniste) > Tehtava.id_laskija:
            print('virheellinen syöte')
        else:
            self.tilauskirja.merkkaa_valmiiksi(int(tunniste))
            print('merkitty valmiiksi')

    def koodarit(self):
        for i in self.tilauskirja.koodarit():
            print(i)

    def koodarin_status(self):
        koodari = input('koodari:')
        if koodari not in self.tilauskirja.koodarit():
            print('virheellinen syöte')
        else:
            tyot = self.tilauskirja.koodarin_status(koodari)
            print(
                f'työt: valmiina {tyot[0]} ei valmiina {tyot[1]}, tunteja: tehty {tyot[2]} tekemättä {tyot[3]}')

    def suorita(self):
        self.ohje()
        while True:
            komento = int(input('komento:'))
            if komento == 0:
                break
            elif komento == 1:
                self.lisaa_tilaus()
            elif komento == 2:
                self.valmiit()
            elif komento == 3:
                self.ei_valmiit()
            elif komento == 4:
                self.merkitse_valmiiksi()
            elif komento == 5:
                self.koodarit()
            elif komento == 6:
                self.koodarin_status()


sovellus = Sovellus()
sovellus.suorita()
