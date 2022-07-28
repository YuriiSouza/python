#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
idade = date.today().year - (int(input("Ano de nascimento: ")))
sexo = int(input('''Qual seu sexo
[ 1 ] Masculino;
[ 2 ] Feminino;'''))

if sexo == 1:
    if idade < 18:
        n = 18 - idade;
        print("Você tem {} anos".format(idade))
        print("Faltam {} anos para o seu alistamente.".format(n))
        print("Seu alistament será em {}".format(date.today().year + 2))
    elif idade == 18:
        print("Voê tem {} ano".format(idade))
        print("Está no ano do seu alistamento")
    elif idade > 18:
        n = idade - 18;
        print("Você tem {} anos".format(idade))
        print("Passaram {} anos do seu alistamento obrigátorio.".format(n))
        print("Seu alistamento foi em {}".format(date.today().year - n))
elif sexo == 2:
    print("Você não precisa se alistar.")
else:
    print("ERRO...")