#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1 + n2)/2;
print("A média é {}".format(media))
if media < 5.0:
    print("REPROVADO")
elif media > 5.0 and media < 6.9:
    print("RECUPEREÇÃO")
else:
    print("APROVADO")
