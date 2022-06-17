# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

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

print(f"The value of R$1000 plus R${val} is R${increased:0.2f}")
