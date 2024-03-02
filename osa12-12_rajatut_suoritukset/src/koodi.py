class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"


def hyvaksytyt(suoritukset: list):
    return filter(lambda x: x.arvosana >= 1, suoritukset)


def suoritus_arvosanalla(suoritukset: list, arvosana: int):
    return filter(lambda x: x.arvosana == arvosana, suoritukset)


def kurssin_suorittajat(suoritukset: list, kurssi: str):
    suorittaneet = filter(lambda x: x.kurssi ==
                          kurssi and x.arvosana > 0, suoritukset)

    return sorted(map(lambda x: x.opiskelijan_nimi, suorittaneet))
