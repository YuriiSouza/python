
frase1 = 'Abacate bom'

print("Mostrando que a variavel é imutavel até atribuirmos algo novo a ela:")
print(frase1)

frase1.upper()

print(frase1)
frase1 = frase1.upper()
print(frase1)

print("-"*30)
print("Mostrando como printar mais de um linha em um mesmo print(): ")
print('''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.''')

print("-"*30)
print("Mostrando a fatiação de strings da linguagem python: ")

frase = "oia so mais quem diria..."

print(frase[3::3])
print(frase[::2])

print("-"*30)
print("Mostrando como ver a quantidade de caracteres de uma variável string: ")

n = len(frase)

print("Número de termos da frase '", frase,"' é ", n)

print("-"*30)
print("Mostrando como uma palavra por outra: ")
print(frase.replace('diria', 'joão'))

print("-"*30)
print("Mostando como separar a frase: ")
listaDaFrase = frase.split()
print(listaDaFrase[0])
print(listaDaFrase[1])
print(listaDaFrase[2])
print(listaDaFrase[3])
print(listaDaFrase[4])
print(listaDaFrase)

print("-"*30)
print("Mostando como juntar as strings presentes em um array: ")
print('--'.join(listaDaFrase))

print("-"*30)
print("Mostando como encontrar um char em uma varialvel str: ")
print(frase.find('a'))
#se retornar um -1 é porque o caracter não existe na variável selecionada.

print("-"*30)
print("Mostrando como saber se em uma variável str tem um sequencia de caracteres: ")
print('a' in frase)
print('x' in frase)
