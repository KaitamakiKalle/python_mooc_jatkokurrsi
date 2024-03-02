# Tee ratkaisusi luokan Auto perään
# Älä muuta luokkaa!
class Auto:
    def __init__(self, merkki: str, huippunopeus: int):
        self.merkki = merkki
        self.huippunopeus = huippunopeus

    def __str__(self):
        return f"Auto (merkki: {self.merkki}, huippunopeus: {self.huippunopeus})"

# TEE RATKAISUSI TÄHÄN:


def nopein_auto(autot: list):
    nopein_auto = autot[0]
    for i in autot:
        if i.huippunopeus > nopein_auto.huippunopeus:
            nopein_auto = i

    return nopein_auto.merkki
