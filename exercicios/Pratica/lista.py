from time import sleep
#Criando lista.
lista = [0, 1, 2, 3, 4, 5, 6]

#Demonstrando como funciona a troca de valor por indice
print(lista[2])
lista[2] = 5
sleep(0.5)
print("Alterando dados", end = '')
print(".", end = '')
sleep(0.5)
print(".", end = '')
sleep(0.5)
print(".")
sleep(0.6)
print(lista[2])

#Adcionando um indice ao fim da lista com um novo elemento usando .append
print("Carregando novos dados", end = '')
print(".", end = '')
sleep(0.5)
print(".", end = '')
sleep(0.5)
print(".")
sleep(0.6)
print(lista[len(lista)-1])
print(lista)
lista.append(10)
print("Alterando dados", end = '')
sleep(1)
print(".", end = '')
sleep(0.5)
print(".", end = '')
sleep(0.5)
print(".")
sleep(0.6)
print(lista[len(lista)-1])
print(f"Lista atual: {lista}")

# 
print("Carregando novos dados", end = '')
print(".", end = '')
sleep(0.5)
print(".", end = '')
sleep(0.5)
print(".")
sleep(0.6)
