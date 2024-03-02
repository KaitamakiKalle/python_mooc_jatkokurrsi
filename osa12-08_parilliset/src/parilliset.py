# TEE RATKAISUSI TÄHÄN:

def parilliset(alku: int, maksimi: int):
    while alku <= maksimi:
        if alku % 2 == 0:
            yield alku
        alku += 1
