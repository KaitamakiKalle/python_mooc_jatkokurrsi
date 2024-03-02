# Tee ratkaisusi tähän:
# Tee ratkaisusi tähän:
class Kello:
    def __init__(self, tunnit: int = 0, minuutit: int = 0, sekunnit: int = 0):
        self.sekunnit = sekunnit
        self.minuutit = minuutit
        self.tunnit = tunnit

    def tick(self):
        if self.sekunnit < 60:
            self.sekunnit += 1

        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1

        if self.minuutit == 60:
            self.minuutit = 0
            self.sekunnit = 0
            self.tunnit += 1

        if self.tunnit == 24:
            self.minuutit = 0
            self.sekunnit = 0
            self.tunnit = 0

    def aseta(self, tunnit: int, minuutit: int):

        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = 0

    def __str__(self):
        return f'{self.tunnit if self.tunnit > 9 else "0" + str(self.tunnit)}:{self.minuutit if self.minuutit > 9 else "0" + str(self.minuutit)}:{self.sekunnit if self.sekunnit > 9 else "0" + str(self.sekunnit)}'
