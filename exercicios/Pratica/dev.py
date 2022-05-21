def mensagem(msn):
    print("-="*12)
    print(f'{msn:^24}')
    print("=-"*12)
def soma(a, b):
    print(f"A soma de {a} com {b} é {a + b}")
def contador(*num):
    print(f"Foram inseridos {len(num)} valores")
def dobra(lista):
    n = 0
    for n in range(0, len(lista)):
        lista[n] = lista[n] * 2
    print(lista)

mensagem("Abacate")

mensagem("Espinafre")

mensagem("Jilo")

soma(3, 5)

soma(a = 3, b = 5)

soma(b = 3, a = 8)

contador(3, 4, 4, 1, 5)

contador(3, 5, 1, 61)

list1 = [1, 3, 5, 12, 6, 1, 61]

dobra(list1)
