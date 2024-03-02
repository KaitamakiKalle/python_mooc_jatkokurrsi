# TEE RATKAISUSI TÄHÄN:

def alkuluvut():
    luku = 2
    while True:
        onko_alkuluku = True
        for i in range(2, luku):
            if luku % i == 0:
                onko_alkuluku = False
                break

        if onko_alkuluku:
            yield luku
        luku += 1
