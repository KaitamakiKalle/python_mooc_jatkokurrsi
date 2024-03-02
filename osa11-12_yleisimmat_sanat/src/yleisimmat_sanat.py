# TEE RATKAISUSI TÄHÄN:

def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    sanat = []
    with open(tiedoston_nimi, 'r') as tiedosto:
        for line in tiedosto:
            sanat.extend(line.split())
    sanat = [sana.strip(',. ') for sana in sanat]
    return {sana: sanat.count(sana) for sana in sanat if sanat.count(sana) >= raja}
