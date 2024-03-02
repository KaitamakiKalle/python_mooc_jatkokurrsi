# TEE RATKAISUSI TÄHÄN:

class Paivays:

    def __init__(self, paiva: int, kuukausi: int, vuosi: int):
        if paiva > 30 or paiva <= 0:
            raise ValueError()
        self._paiva = paiva

        if kuukausi > 12 or kuukausi <= 0:
            raise ValueError()
        self._kuukausi = kuukausi

        self._vuosi = vuosi

    def __str__(self):
        return f'{self._paiva}.{self._kuukausi}.{self._vuosi}'

    def __lt__(self, toinen: 'Paivays'):
        return (self._vuosi, self._kuukausi, self._paiva) < (toinen._vuosi, toinen._kuukausi, toinen._paiva)

    def __gt__(self, toinen: 'Paivays'):
        return (self._vuosi, self._kuukausi, self._paiva) > (toinen._vuosi, toinen._kuukausi, toinen._paiva)

    def __eq__(self, toinen: 'Paivays'):
        return (self._vuosi, self._kuukausi, self._paiva) == (toinen._vuosi, toinen._kuukausi, toinen._paiva)

    def __ne__(self, toinen: 'Paivays'):
        return (self._vuosi, self._kuukausi, self._paiva) != (toinen._vuosi, toinen._kuukausi, toinen._paiva)

    def __add__(self, lisays: int):

        paiva = self._paiva
        kuukausi = self._kuukausi
        vuosi = self._vuosi

        while lisays > 0:
            if paiva + lisays > 30:

                lisays -= 30 - paiva + 1

                paiva = 1
                if kuukausi + 1 > 12:
                    kuukausi = 1
                    vuosi += 1
                else:
                    kuukausi += 1
            else:
                paiva += lisays
                lisays -= lisays

        return Paivays(paiva, kuukausi, vuosi)

    def __sub__(self, toinen: 'Paivays'):

        paivat1 = self._paiva + 30 * self._kuukausi + self._vuosi * 360

        paivat2 = toinen._paiva + 30 * toinen._kuukausi + toinen._vuosi * 360

        return (paivat1 - paivat2) * -1 if paivat1 - paivat2 < 0 else paivat1 - paivat2
