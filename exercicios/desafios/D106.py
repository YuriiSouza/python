#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
def printa(msn):
    n = (len(msn)+4)
    print('=' * n)
    print(f'  {msn}  ')
    print("=" * n)


while True:
    fuc = str(input("Biblioteca ou função: "))

    if fuc == 'fim':
        break
    
    printa(f"The manual of the {fuc}")
    print(help(fuc))
    