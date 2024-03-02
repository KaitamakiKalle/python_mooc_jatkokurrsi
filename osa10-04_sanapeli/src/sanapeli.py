# TEE RATKAISUSI TÄHÄN:
import random


class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass  # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")


class PisinSana(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1
        elif len(pelaaja1_sana) < len(pelaaja2_sana):
            return 2
        else:
            pass


class EnitenVokaaleja(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def __laske_vokaalit(self, sana: str):
        vokaalit = 0

        for i in sana.lower():
            if i in 'eyuioåaöä':
                vokaalit += 1
        return vokaalit

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        pelaaja1_vokaalit = self.__laske_vokaalit(pelaaja1_sana)
        pelaaja2_vokaalit = self.__laske_vokaalit(pelaaja2_sana)

        if pelaaja1_vokaalit > pelaaja2_vokaalit:
            return 1
        elif pelaaja1_vokaalit < pelaaja2_vokaalit:
            return 2
        else:
            pass


class KiviPaperiSakset(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        sanat = ['kivi', 'paperi', 'sakset']

        if (pelaaja1_sana == 'kivi' and pelaaja2_sana == 'sakset') or (pelaaja1_sana == 'sakset' and pelaaja2_sana == 'paperi') or (pelaaja1_sana == 'paperi' and pelaaja2_sana == 'kivi') or (pelaaja2_sana not in sanat and pelaaja1_sana in sanat):
            return 1
        elif (pelaaja2_sana == 'kivi' and pelaaja1_sana == 'sakset') or (pelaaja2_sana == 'sakset' and pelaaja1_sana == 'paperi') or (pelaaja2_sana == 'paperi' and pelaaja1_sana == 'kivi') or (pelaaja1_sana not in sanat and pelaaja2_sana in sanat):
            return 2
        else:
            pass
