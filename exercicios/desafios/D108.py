# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
import moeda

val = str(input("value: R$"))

if ',' in val:
  val = float(val.replace(',', '.'))
  double = moeda.double(val)
  print(f"The double is R${double},00")
else:
  val = float(val)
  double = moeda.double(val)
  print(f"The double is R${double:0.2f}")

increased = moeda.increase(val, 1000)

print(f"The value of R$1000 plus R${val} is", end = ' ')
moeda.print_formatted(increased)
