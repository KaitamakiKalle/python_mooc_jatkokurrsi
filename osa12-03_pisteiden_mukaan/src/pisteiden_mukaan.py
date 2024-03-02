# TEE RATKAISUSI TÄHÄN:
def jarjesta_pisteiden_mukaan(alkiot: list):
    def kausi_jarjestys(alkio: dict):
        return alkio['pisteet']
    return sorted(alkiot, key=kausi_jarjestys, reverse=True)
