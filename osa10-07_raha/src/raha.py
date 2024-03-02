# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self._eurot = eurot
        self._sentit = sentit

    def __str__(self):
        return f"{self._eurot}.{'0' + str(self._sentit) if self._sentit < 10 else self._sentit} eur"

    def __eq__(self, toinen: 'Raha'):
        if self._eurot == toinen._eurot and self._sentit == toinen._sentit:
            return True
        else:
            return False

    def __lt__(self, toinen: 'Raha'):
        if float(f"{self._eurot}.{'0' + str(self._sentit) if self._sentit < 10 else self._sentit}") < float(f"{toinen._eurot}.{'0' + str(toinen._sentit) if toinen._sentit < 10 else toinen._sentit}"):
            return True
        else:
            return False

    def __gt__(self, toinen: 'Raha'):
        if float(f"{self._eurot}.{'0' + str(self._sentit) if self._sentit < 10 else self._sentit}") <= float(f"{toinen._eurot}.{'0' + str(toinen._sentit) if toinen._sentit < 10 else toinen._sentit}"):
            return False
        else:
            return True

    def __add__(self, toinen: 'Raha'):

        eurot = self._eurot + toinen._eurot
        sentit = 0
        if self._sentit + toinen._sentit >= 100:
            eurot += 1
            sentit = self._sentit + toinen._sentit - 100
        else:
            sentit = self._sentit + toinen._sentit

        return Raha(eurot, sentit)

    def __sub__(self, toinen: 'Raha'):

        eurot = self._eurot - toinen._eurot
        sentit = self._sentit - toinen._sentit

        if sentit < 0:
            if eurot < 0:
                eurot += 1
                sentit += 100
            else:
                eurot -= 1
                sentit += 100

        if eurot < 0 or sentit < 0:
            raise ValueError()
        return Raha(eurot, sentit)
