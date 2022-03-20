#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = 'abacate', 'tomate', 'joao', 'lucas', 'refrigerante'

for n in range(0, 5):
    j = tupla[n].split()
    print(f"{j} Tem as vogais: ")
    for x in range(0, len(j)):
        if  'a' in j[x]:
            print('a')
        if  'e' in j[x]:
            print('e')
        if  'i' in j[x]:
            print('i')
        if  'o' in j[x]:
            print('o')
        if  'u' in j[x]:
            print('u')    
        