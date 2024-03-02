class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

# Tee ratkaisusi tähän:


def pituuden_mukaan(reitit: list):
    def pituus_jarjestys(alkio: 'Kiipeilyreitti'):
        return alkio.pituus
    return sorted(reitit, key=pituus_jarjestys, reverse=True)


def vaikeuden_mukaan(reitit: list):
    def vaikeus_jarjestys(alkio: 'Kiipeilyreitti'):
        return (alkio.grade, alkio.pituus)
    return sorted(reitit, key=vaikeus_jarjestys, reverse=True)
