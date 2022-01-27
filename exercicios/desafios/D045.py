#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print("=-=_"*10)
print("jOkEnPô")
print("=-=_"*10)

while True:
    jokenpo = ['pedra','papel','tesoura']
    n = int(input('''Escolha:
    [1]==pedra
    [2]==papel
    [3]==tesoura\n'''))

    y = randint(1,3)
    print(f"Sua escolha: {jokenpo[n-1]}\n")
    print(f"Escolha da IA: {jokenpo[y-1]}\n")
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ!!!")
    sleep(1)

    if n == y:
        print("EMPATE...")
    elif (y == 2 and n == 1) or (y == 3 and n == 2) or (y == 1 and n == 3):
        print("IA ganha, mais sorte na proxima...")
    elif (n == 1 and y == 3) or (n == 2 and y == 1) or (n == 3 and y == 2):
        print("Você GANHOU, parabéns.")
    else:
        print("ERRO")

    continuar = str(input("Continuar S OU N: ")).lower()
    
    if continuar == 'n':
        break
