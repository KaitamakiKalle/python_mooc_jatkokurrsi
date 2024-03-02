# TEE RATKAISUSI TÄHÄN:

def jarjesta_tuotantokausien_mukaan(alkiot: list):
    def kausi_jarjestys(alkio: dict):
        return alkio['kausia']
    return sorted(alkiot, key=kausi_jarjestys)
