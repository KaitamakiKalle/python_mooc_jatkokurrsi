# tee ratkaisusi tänne
import json


class Tilasto:

    def __init__(self, tiedosto: str):
        self.__tiedosto = tiedosto,
        self.__data = Tilasto.lue_json(tiedosto)

    @classmethod
    def lue_json(cls, tiedosto: str):
        with open(tiedosto) as tiedosto:
            data = tiedosto.read()
        return json.loads(data)

    @property
    def data(self):
        return self.__data

    def hae_pelaaja(self, pelaaja_nimi: str):
        # Filtteröidään oikea pelaaja listasta
        pelaaja = list(
            filter(lambda x: x['name'] == pelaaja_nimi, self.__data))
        # Koska filteröinnin tuloksena muodostuu lista otetaan sen ensimmäinen ja ainut alkio joka on haettu pelaaja
        return pelaaja[0]

    def hae_joukkueiden_lyhenteet(self):
        return sorted(set(map(lambda x: x['team'], self.data)))

    def hae_maiden_nimet(self):
        return sorted(set(map(lambda x: x['nationality'], self.data)))


class Sovellus:

    def __init__(self, tiedosto: str):
        self.__tilasto = Tilasto(tiedosto)
        print(f'luettiin {len(self.__tilasto.data)} pelaajan tiedot')

    def ohje(self):
        print('komennot:')
        print("0 lopeta")
        print("1 hae pelaaja")
        print("2 joukkueet")
        print("3 maat")
        print("4 joukkueen pelaajat")
        print("5 maan pelaajat")
        print("6 eniten pisteitä")
        print("7 eniten maaleja")

    def hae_pelaaja(self):
        nimi = input('nimi:')
        pelaaja = self.__tilasto.hae_pelaaja(nimi)
        print(f'{pelaaja["name"]:<20} {pelaaja["team"]:<4} {pelaaja["goals"]:>2} + {pelaaja["assists"]:>2} = {pelaaja["goals"] + pelaaja["assists"]:>3}')

    def joukkueet(self):
        joukkueet = self.__tilasto.hae_joukkueiden_lyhenteet()
        for i in joukkueet:
            print(i)

    def maat(self):
        maat = self.__tilasto.hae_maiden_nimet()
        for i in maat:
            print(i)

    def suorita(self):
        self.ohje()
        # print(self.__tilasto.data)
        while True:
            komento = input('komento:')

            if komento == '0':
                break
            elif komento == '1':
                self.hae_pelaaja()
            elif komento == '2':
                self.joukkueet()
            elif komento == '3':
                self.maat()


tiedosto = input('tiedosto:')
sovellus = Sovellus(tiedosto)
sovellus.suorita()

# Alex Ovechkin        WSH  48 + 19 =  67
# Alex Ovechkin        WSH   48 + 19 =  67
