from modulo_ex115 import *

create_file('data.txt')

while True:
    var_resp = print_menu(('Adcionar pessoa', 'Mostrar lista', 'Sair'))
    if var_resp == 1:#Adicionar
        cadastrar('data.txt')

    elif var_resp == 2:# Mostrar lista
        mostra('data.txt')

    elif var_resp == 3:# Sair
        cabecalho('FIM')
        break
