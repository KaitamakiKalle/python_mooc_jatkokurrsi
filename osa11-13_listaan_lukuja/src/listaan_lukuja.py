# TEE RATKAISUSI TÄHÄN:

def listaan_lukuja(luvut: list):
    if len(luvut) % 5 != 0:
        luvut.append(luvut[len(luvut) - 1] + 1)
        listaan_lukuja(luvut)
