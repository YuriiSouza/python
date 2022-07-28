lista = [1, 2, 3, 4]

lista2 = lista[:]#copia
lista1 = lista#associadas

del lista1[1]
print(lista1)

lista1.pop(2)
print(lista1)

lista1.remove(3)
print(lista1)

print(lista)
print(lista2)
