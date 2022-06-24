from re import X


def linha(tam = 30):
    print('='*tam)


def cabecalho(msn):
    linha()
    print(msn.center(30))
    linha()


def print_menu(lista):
    cabecalho('Sistema')
    c = 1
    for x in lista:
        print(f'{c} -- > {x}')
        c += 1
     
    return leia_int('-->> ')


def leia_int(mensagem):
    while True:
        try:   
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print("Valor inválido!!!")
        except (KeyboardInterrupt):
            print("Quis parar...")
            break
        else:
            return n


def leia_float(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except(ValueError, TypeError):
            print("Valor inválido...")
        except (KeyboardInterrupt):
            print("Saiu")
            break
        else:
            return n


def create_file(name):
    try:
        open(name, 'x')
    except:
        print("Status: File exist...")

