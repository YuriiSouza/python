from modulo_ex115 import *


create_file('data.txt')
nome = list()

while True:
    var_resp = print_menu(('Adcionar pessoa', 'Mostrar lista', 'Sair'))
    if var_resp == 1:#Adicionar
        data = open('data.txt', 'a')
        data.writelines('[')
        data.writelines(str(input("Nome: ")))
        data.writelines(' , ')
        data.writelines(str(input("Idade: ")))
        data.writelines(']')
    elif var_resp == 2:# Mostrar lista
        data = open('data.txt', 'r')
        nome = data.readlines()
        for n in nome:
            print(f'{n[0]}      {n[1]}')
    elif var_resp == 3:# Sair
        print('3')
        cabecalho('FIM')
        break
