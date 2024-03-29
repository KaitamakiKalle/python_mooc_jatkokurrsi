class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"

# Tee ratkaisusi tähän:


def suorittajien_nimet(suoritukset: list):
    return list(map(lambda x: x.opiskelijan_nimi, suoritukset))


def kurssien_nimet(suoritukset: list):
    return sorted(set(map(lambda x: x.kurssi, suoritukset)), key=lambda x: x)
