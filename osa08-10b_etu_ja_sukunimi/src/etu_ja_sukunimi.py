# Tee ratkaisusi tähän

class Henkilo:
    
    def __init__(self, nimi: str):
        self.nimi = nimi

    def anna_etunimi(self):
        return self.nimi[:self.nimi.find(' ')]

    def anna_sukunimi(self):
        return self.nimi[self.nimi.find(' ') + 1:]







