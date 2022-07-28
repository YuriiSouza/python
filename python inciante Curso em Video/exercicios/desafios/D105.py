#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(*num, sit = False):
    '''
    Essa função faz coisas incriveis, coloque sit = True para ser retornado a situação do aluno referente as notas
    '''
    dicta = dict()
    cont = maior = menor = soma1 = 0
    dicta['quant'] = len(num)
    for n in num:
        if cont == 0:
            maior = n
            menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
        cont += 1
    dicta['maior'] = maior
    dicta['menor'] = menor
    dicta['media'] = sum(num)/len(num)
    if sit == True:
        if dicta['media'] > 6:
            dicta['situação'] = 'Bom'
        elif dicta['media'] < 5.9 or dicta['media'] > 4:
            dicta['situação'] = 'Mediano'
        elif dicta['media']:
            dicta['situação'] = 'Ruim'
    
    return dicta



resp = notas(9, 3, 8, sit = True)
print(resp)
help(notas)