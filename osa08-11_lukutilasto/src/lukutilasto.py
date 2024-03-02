# Tee ratkaisusi tähän:
class Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.luvut = []

    def lisaa_luku(self, luku:int):
        self.lukuja += 1
        self.luvut.append(luku)

    def lukujen_maara(self):
        return self.lukuja

    def summa(self):
        return sum(self.luvut) if self.lukuja > 0 else 0

    def keskiarvo(self):
        return self.summa() / self.lukuja if self.lukuja > 0 else 0
    
    
luvut = Lukutilasto()
parilliset = Lukutilasto()
parittomat = Lukutilasto()

print('Anna lukuja:')

while True:
    syote = int(input())

    if syote == -1:
        break
    else:
        luvut.lisaa_luku(syote)
        if syote % 2 == 0:
            parilliset.lisaa_luku(syote)
        else:
            parittomat.lisaa_luku(syote)

print('Summa:', luvut.summa())
print('Keskiarvo:', luvut.keskiarvo())
print('Parillisten summa:', parilliset.summa())
print('Parittomien summa:', parittomat.summa())
