# tee ratkaisusi tänne
class KurssiSuoritus:
    def __init__(self, nimi: str, arvosana: int, opintopisteet: int):
        self.__nimi = nimi
        self.__arvosana = arvosana
        self.__opintopisteet = opintopisteet

    def nimi(self):
        return self.__nimi

    def arvosana(self):
        return self.__arvosana

    def korota_arvosanaa(self, arvosana: int):
        if arvosana > self.__arvosana and arvosana <= 5:
            self.__arvosana = arvosana

    def opintopisteet(self):
        return self.__opintopisteet


class Opiskelija:
    def __init__(self):
        self.__suoritukset = {}
        self.__opintopisteet = 0

    def lisaa_suoritus(self, kurssi: str, arvosana: int, opintopisteet: int):
        if kurssi not in self.__suoritukset:
            self.__suoritukset[kurssi] = KurssiSuoritus(
                kurssi, int(arvosana), int(opintopisteet))
            self.__opintopisteet += int(opintopisteet)
        else:
            self.__suoritukset[kurssi].korota_arvosanaa(int(arvosana))

    def hae_suoritus(self, kurssi: str):
        if kurssi not in self.__suoritukset:
            return None
        kurssi = self.__suoritukset[kurssi]
        return f'{kurssi.nimi()} ({kurssi.opintopisteet()} op) arvosana {kurssi.arvosana()}'

    def tilasto(self):
        arvosanajakauma = {
            'ykköset': 0,
            'kakkoset': 0,
            'kolmoset': 0,
            'neloset': 0,
            'vitoset': 0,
        }
        summa = 0
        for i in self.__suoritukset:

            summa += self.__suoritukset[i].arvosana()
            if self.__suoritukset[i].arvosana() == 1:
                arvosanajakauma["ykköset"] += 1
            elif self.__suoritukset[i].arvosana() == 2:
                arvosanajakauma["kakkoset"] += 1
            elif self.__suoritukset[i].arvosana() == 3:
                arvosanajakauma["kolmoset"] += 1
            elif self.__suoritukset[i].arvosana() == 4:
                arvosanajakauma["neloset"] += 1
            elif self.__suoritukset[i].arvosana() == 5:
                arvosanajakauma["vitoset"] += 1
        keskiarvo = summa/len(self.__suoritukset)

        return {
            'opintopisteet': self.__opintopisteet,
            'kurssien_lkm': len(self.__suoritukset),
            'keskiarvo': round(keskiarvo, 1),
            'arvosanajakauma': arvosanajakauma

        }


class Sovellus:
    def __init__(self):
        self.__opiskelija = Opiskelija()

    def ohje(self):
        print("komennot: ")
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")

    def suorituksen_lisays(self):
        kurssi = input('kurssi: ')
        arvosana = input('arvosana: ')
        opintopisteet = input('opintopisteet: ')

        self.__opiskelija.lisaa_suoritus(kurssi, arvosana, opintopisteet)

    def suorituksen_haku(self):
        kurssi = input('kurssi: ')
        suoritus = self.__opiskelija.hae_suoritus(kurssi)
        if suoritus == None:
            print('ei suoritusta')
            return
        print(suoritus)

    def tilasto(self):
        tilasto = self.__opiskelija.tilasto()

        print(
            f'suorituksia {tilasto["kurssien_lkm"]} kurssilta, yhteensä {tilasto["opintopisteet"]} opintopistettä')
        print(f'keskiarvo {tilasto["keskiarvo"]}')
        print('arvosanajakauma')
        print(f'5: {"x" * tilasto["arvosanajakauma"]["vitoset"]}')
        print(f'4: {"x" * tilasto["arvosanajakauma"]["neloset"]}')
        print(f'3: {"x" * tilasto["arvosanajakauma"]["kolmoset"]}')
        print(f'2: {"x" * tilasto["arvosanajakauma"]["kakkoset"]}')
        print(f'1: {"x" * tilasto["arvosanajakauma"]["ykköset"]}')

    def suorita(self):
        self.ohje()
        while True:
            komento = input('komento: ')
            if komento == '0':
                break
            elif komento == '1':
                self.suorituksen_lisays()
            elif komento == '2':
                self.suorituksen_haku()
            elif komento == '3':
                self.tilasto()


sovellus = Sovellus()
sovellus.suorita()
