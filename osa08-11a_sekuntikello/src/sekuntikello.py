# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0

    def tick(self):
        if self.sekunnit < 60:
            self.sekunnit += 1

        if self.sekunnit == 60:
                self.sekunnit = 0
                self.minuutit += 1
        
        if self.minuutit == 60:
            self.minuutit = 0
            self.sekunnit = 0
    
    def __str__(self):
         return f'{self.minuutit if self.minuutit > 9 else "0" + str(self.minuutit)}:{self.sekunnit if self.sekunnit > 9 else "0" + str(self.sekunnit)}'