# Adapte o c�digo do desafio #107, criando uma fun��o adicional chamada moeda() que consiga mostrar os n�meros como um valor monet�rio formatado.
import moeda

form = str(input("Do you wanna the formatted mode?")).lower()[0]
val = str(input("value: R$"))

if ',' in val:
  val = float(val.replace(',', '.'))
  if form == 'y':
    double = moeda.double(val, True)
  else:
    double = moeda.double(val)
  print(f"The double is R${double},00")
  
else:
  val = float(val)
  f form == 'y':
    double = moeda.double(val, True)
  else:
    double = moeda.double(val)
  print(f"The double is {double}")

increased = moeda.increase(val, 1000)

print(f"The value of R$1000 plus R${val} is",moeda.formatted(increased))
