# Tee ratkaisusi luokan Koesuoritus perään.
# ÄLÄ MUUTA LUOKKAA
class Koesuoritus:
    def __init__(self, suorittaja: str, pisteet: int):
        self.suorittaja = suorittaja
        self.pisteet = pisteet

    def __str__(self):
        return f'Koesuoritus (suorittaja: {self.suorittaja}, pisteet: {self.pisteet})'

# TEE RATKAISUSI TÄHÄN:


def hyvaksytyt(suoritukset: list, pisteraja: int):
    lapaisseet = []
    for i in suoritukset:
        if i.pisteet >= pisteraja:
            lapaisseet.append(i)
    return lapaisseet
