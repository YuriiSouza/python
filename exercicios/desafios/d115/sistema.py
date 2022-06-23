from modulo_ex115 import *

while True:
    try:
        while True:
            var_resp = print_menu(('Adcionar pessoa', 'Mostrar lista', 'Sair'))
            if var_resp == 1:#Adicionar
                print('1')
            elif var_resp == 2:# Mostrar lista
                print('2')
            elif var_resp == 3:# Sair
                print('3')
                cabecalho('FIM')
                break
        break
    except (ValueError, TypeError):
        print('Error, valor inválido...')
