# tee ratkaisu tänne


def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):

    def keskiarvo(luvut: list):
        return sum(luvut) / len(luvut)

    henkilot = [henkilo1, henkilo2, henkilo3]
    pienin = henkilo1

    for x in henkilot:

        if keskiarvo([x["tulos1"], x["tulos2"], x["tulos3"]]) < keskiarvo([pienin["tulos1"], pienin["tulos2"], pienin["tulos3"]]):
            pienin = x
    return pienin
