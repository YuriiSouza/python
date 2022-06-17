n = True))def increase(value, increased, formatation = False):
  r = value + increased
  if formatation == True:
    r = formatted(r)
  return r


def decreas(value, decreased):
  r = value - decreased
  return r


def double(value):
  r = value * 2
  return r


def aHalf(value):
  r = value / 2


def formatted(value):
  if '.' in str(value):
    value = "R$" + str(value)
  else:
    value = "R$" + str(value) + ",00"

  return value
