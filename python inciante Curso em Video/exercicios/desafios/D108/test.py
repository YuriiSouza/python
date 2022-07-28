# Adapte o c�digo do desafio #107, criando uma fun��o adicional chamada moeda() que consiga mostrar os n�meros como um valor monet�rio formatado.
from  utilidades_dev import moeda

form = str(input("Do you wanna the formatted mode?")).lower()[0]
val = str(input("value: "))

if ',' in val:
  val = float(val.replace(',', '.'))
  if form == 'y':
    double = moeda.double(val, True)
  else:
    double = moeda.double(val)
else:
  val = float(val)
  if form == 'y':
    double = moeda.double(val, True)
  else:
    double = moeda.double(val)

print(f"The double is {double}")

if form == 'y':
  increased = moeda.increase(val, 10, True)
else:
  increased = moeda.increase(val, 10)  

print(f"The price with 10% is {increased} ")
