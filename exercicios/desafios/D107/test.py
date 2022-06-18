# Crie um modulo chamado moeda.py que tenha as fun��es incorporadas aumentar(), diminuir(), dobro() e metade(). Fa�a tamb�m um programa que importe esse m�dulo e use algumas dessas fun��es.

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

print(f"The value of 1000% of R${val} is R${increased:0.2f}")
