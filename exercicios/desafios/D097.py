#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def printa(msn):
    n = (len(msn)+4)
    print('=' * n)
    print(f'  {msn}  ')
    print("=" * n)


#Programa principal
while True:
    while True:
        n = str(input("Frase: "))
        if n not in "":
            break

    printa(n)

    while True:
        deseja = str(input("Deseja continuar? ")).lower()[0]
        if deseja in 'sn':
            break
    
    if deseja == 'n':
        break
