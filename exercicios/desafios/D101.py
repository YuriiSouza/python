# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(anoNasc):
    from datetime import date

    idade = date.today().year - anoNasc
    status = ''
    
    if idade > 60:
        status = 'OPCIONAL'
    elif idade > 16:
        status = 'OBRIGATORIO'
    elif idade < 16:
        status = 'NÃO VOTA'

    return ('O cidadão tem ', idade, ' seu voto é ', status)



ano = int(input("Ano de nascimento: "))

print(voto(ano))
