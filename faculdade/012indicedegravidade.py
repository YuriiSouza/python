#numero 4
from time import sleep
from random import randint

cont = 0
while True:
    indice_de_gravidade = randint(0, 10)
    
    if indice_de_gravidade > 9:
        print("Grave")
        cont = cont + 1
        sleep(1)
    else:
        print(".")
        sleep(1)
        
    if cont >= 3:
        print("explodiu")
        sleep(2)
        break
    