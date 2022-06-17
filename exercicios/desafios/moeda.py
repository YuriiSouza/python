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


def formatted(value):
  if '.' in str(value):
    value = "R$" + str(value)
  else:
    value = "R$" + str(value) + ",00"

  return value
