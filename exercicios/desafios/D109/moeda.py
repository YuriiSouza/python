def increase(value, increased, formatation = False):
  r = value + increased

  return r if formatation == False else formatted(r)


def decreas(value, decreased, formatation = False):
  r = value - decreased
  
  return r if formatation == False else formatted(r)


def double(value, formatation = False):
  r = value * 2
  
  return r if formatation == False else formatted(r)


def aHalf(value, formatation = False):
  r = value / 2
 
  return r if formatation == False else formatted(r)



def formatted(value, tipe = 'R$'):
    return f'{tipe}{value:.2f}'.replace('.', ',')


