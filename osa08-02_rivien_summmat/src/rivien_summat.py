# tee ratkaisu tänne
# Listan alkioiden arvot ovat viittauksia olioihin. Tämä pätee myös silloin, kun mallinnetaan matriisia:
# jokainen päälistan alkion arvo on viittaus toiseen listaan(jonka alkiot taas ovat viittauksia arvoihin).

# Tee funktio rivien_summat(matriisi: list), joka saa parametrikseen kokonaislukuja sisältävän matriisin.

# Funktio lisää jokaiselle matriisin riville uuden alkion, jonka arvo on rivin alkioiden summa.
# Funktio ei palauta mitään, vaan muokkaa parametrinaan saamaansa matriisia.


def rivien_summat(matriisi: list):

    for x in matriisi:
        x.append(sum(x))
