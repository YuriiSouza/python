def increase(value, increased, formatation = False):
    r = value + (value*increased)/100
    return r if formatation == False else formatted(r)



def decreas(value, decreased, formatation = False):
    r = value - (value * decreased)/100
    return r if formatation == False else formatted(r)



def double(value, formatation = False):
    r = value * 2
    return r if formatation == False else formatted(r)



def a_half(value, formatation = False):
    r = value / 2
    return r if formatation == False else formatted(r)


def formatted(value, tipe = 'R$'):
    return f'{tipe}{value:.2f}'.replace('.', ',')


def resume_value(value, rate_up, rate_down):
    print("+-"*10)
    print(f"{'Resume':^20}")
    print("+-"*10)

    print(f'The price with {rate_up}% of increased is {increase(value, rate_up, True)}')
    
    print(f'The price with {rate_down}% of decreased is {increase(value, rate_down, True)}')

    print(f'The double price is {double(value, True)}')

    print(f'The a half of price is {a_half(value, True)}')
