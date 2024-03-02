# TEE RATKAISUSI TÄHÄN:

def suodata_kielletyt(merkkijono: str, kielletyt: str):
    return ''.join([kirjain for kirjain in merkkijono if kirjain not in kielletyt])
