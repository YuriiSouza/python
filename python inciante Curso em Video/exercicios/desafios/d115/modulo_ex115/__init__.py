def linha(tam = 30):
    print('='*tam)


def cabecalho(msn, tam = 30):
    linha(tam)
    print(msn.center(tam))
    linha(tam)


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
    else:
        print("Status: File was create....")
        

def cadastrar(arq):
    cabecalho('Novo registro')
    try:
        data = open(arq, 'a')
    except:
        print(f"Erro ao tentar abrir arquivo {arq}.")
    else:
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        data.write(f'{nome};{idade}\n')

    
def mostra(arq):
    print(f'{"Nome":<20}{"Idade":>9}')
    linha()
    try:
        d = open(arq, 'r')
    except:
        print(f"Erro ao tentar abrir arquivo {arq}.")
    else:
        for n in d:
            dados = n.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0].capitalize():<20}{dados[1]:>4} anos')
        # print(d.read().replace(';', '\t\t').replace('\n', ' anos\n')) oq eu fiz sozinho

