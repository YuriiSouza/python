algo = input("Digite algo: ")

print(type(algo))
print("Contém somente espaços: ", algo.isspace())
print("É um número: ", algo.isnumeric())
print("É apenas letras: ", algo.isalpha())
print("É alphanumerico: ", algo.isalnum())
print("Esta apenas em maiusculas: ", algo.isupper())
print("Esta apenas em minusculas: ", algo.islower())
print("Esta capitalizado: ", algo.istitle())
  