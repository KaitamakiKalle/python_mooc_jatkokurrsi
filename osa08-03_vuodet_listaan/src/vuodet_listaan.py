# tee ratkaisu tänne
# Muista import-lause:

from datetime import date


def vuodet_listaan(paivamaarat: list):

    vuodet = []
    for x in paivamaarat:
        vuodet.append(x.year)
    vuodet.sort()
    return vuodet
