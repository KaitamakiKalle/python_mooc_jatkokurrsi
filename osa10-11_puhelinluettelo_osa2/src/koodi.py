# Tee ratkaisusi tähän:

class Henkilo:

    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__numerot = []
        self.__osoite = ''

    def nimi(self):
        return self.__nimi

    def numerot(self):
        return self.__numerot

    def lisaa_numero(self, numero: str):
        if len(numero) <= 0:
            raise ValueError
        else:
            self.__numerot.append(numero)

    def osoite(self):
        return None if len(self.__osoite) == 0 else self.__osoite

    def lisaa_osoite(self, osoite: str):

        if len(osoite) <= 0:
            raise ValueError
        else:
            self.__osoite = osoite


class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_numero(numero)

    def lisaa_osoite(self, nimi: str, osoite: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)

        self.__henkilot[nimi].lisaa_osoite(osoite)

    def hae_tiedot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]

    def kaikki_tiedot(self):
        return self.__henkilot


class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")

    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

    def haku(self):
        nimi = input("nimi: ")
        henkilo = self.__luettelo.hae_tiedot(nimi)
        if henkilo == None or len(henkilo.numerot()) == 0:
            print("numero ei tiedossa")

        else:
            for numero in henkilo.numerot():
                print(numero)

        if henkilo == None or henkilo.osoite() == None:
            print('osoite ei tiedossa')
        else:
            print(f'{henkilo.osoite()}')

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()


# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
