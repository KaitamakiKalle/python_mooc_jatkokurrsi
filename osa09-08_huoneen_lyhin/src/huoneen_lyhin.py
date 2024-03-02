# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return f'{self.nimi} ({self.pituus} cm)'


class Huone:

    def __init__(self):
        self.henkilot = []
        self.yhteispituus = 0

    def lisaa(self, henkilo: 'Henkilo'):
        self.henkilot.append(henkilo)
        self.yhteispituus += henkilo.pituus

    def on_tyhja(self):
        return False if len(self.henkilot) > 0 else True

    def tulosta_tiedot(self):
        print(
            f'Huoneessa on {len(self.henkilot)} henkilöä, yhteispituus {self.yhteispituus} cm')
        for i in self.henkilot:
            print(i)

    def lyhin(self):
        if len(self.henkilot) == 0:
            return None

        lyhin = self.henkilot[0]

        for i in self.henkilot:
            if i.pituus < lyhin.pituus:
                lyhin = i

        return lyhin

    def poista_lyhin(self):
        if len(self.henkilot) == 0:
            return None
        poistettava = self.lyhin()
        self.henkilot.remove(poistettava)
        return poistettava
