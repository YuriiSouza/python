#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER
from datetime import date
idade = date.today().year - int(input("Ano de nascimento"))

print('''O atleta tem {} anos.
Ele pertence a seguinte categoria: '''.format(idade))

if idade <= 9:
    print("MIRIM")
elif idade > 9 and idade <= 14:
    print("INFANTIL")
elif idade > 14 and idade <= 19:
    print("JÚNIOR")
elif idade > 19 and idade <= 25:
    print("SÊNIOR")
elif idade > 25:
    print("MASTER")
else:
    print("Não encontrado...")
