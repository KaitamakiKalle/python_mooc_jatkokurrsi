# TEE RATKAISUSI TÄHÄN:
import random


def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    while maara > 0:
        mjono = ''

        for i in range(0, pituus + 1):
            mjono += kirjaimet[random.randint(0, len(kirjaimet) - 1)]

        yield mjono
        maara -= 1
