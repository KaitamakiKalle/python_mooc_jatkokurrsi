# TEE RATKAISUSI TÄHÄN:

def jarjesta_varastosaldon_mukaan(alkiot: list):
    def saldojarjestys(alkio: tuple):
        return alkio[2]

    lista_kopio = [alkio for alkio in alkiot]

    return sorted(lista_kopio, key=saldojarjestys)
