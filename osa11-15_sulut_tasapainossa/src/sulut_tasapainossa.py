
def sulut_tasapainossa(merkkijono: str):
    merkkijono = ''.join([merkki for merkki in merkkijono if merkki in '()[]'])
    if len(merkkijono) == 0:
        return True
    if merkkijono[0] == '(' and merkkijono[-1] != ')':
        return False
    elif merkkijono[0] == '[' and merkkijono[-1] != ']':
        return False
    elif len(merkkijono) == 1 and merkkijono in '()[]':
        return False

    # poistetaan ensimmäinen ja viimeinen merkki
    return sulut_tasapainossa(merkkijono[1:-1])
