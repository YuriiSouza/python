def increase(value, increased, formatation = False):
    r = value + increased
    if formatation == True:
        r = formatted(r)
    return r


def decreas(value, decreased, formatation = False):
    r = value - decreased
    if formatation == True:
        r = formatted(r)

    return r


def double(value, formatation = False):
    r = value * 2
    if formatation == True:
        r = formatted(r)

    return r


def aHalf(value, formatation = False):
    r = value / 2
    if formatation == True:
        r = formatted(r)
    return r


def formatted(value, tipe = 'R$'):
    return f'{tipe}{value:.2f}'.replace('.', ',')
