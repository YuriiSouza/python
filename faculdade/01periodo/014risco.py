#número 6
from time import sleep
from random import randint

cont = 0
while True:
    indice_de_gravidade = randint(0, 10)
    

    if indice_de_gravidade > 9:
        print("Grave")
        cont = cont + 1
        sleep(1)
    elif indice_de_gravidade <= 9 and indice_de_gravidade > 6:
        print("Alto")
        sleep(1)
    elif indice_de_gravidade <= 6 and indice_de_gravidade > 3:
        print("Médio")
        sleep(1)
    elif indice_de_gravidade <= 3 and indice_de_gravidade > 0:
        print("Baixo")
        sleep(1)
    else:
        print(".")
        sleep(1)
        
    if cont >= 3:
        print("explodiu")
        sleep(2)
        break
    