#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra A;
#Qual posição que ela aparece a primeira vez;
#Qual posição que ela aparece a ultima vez;

frase = str(input("Digite um frase: ")).upper().strip()
fraselower = frase.lower()
print("A letra 'A' aparece {} vezes na frase. ".format(fraselower.count('a')))
print("A primeira posição do A foi em {}".format(fraselower.find('a')+1))
print("A ultima posicção de 'A' fou em {}".format(fraselower.rfind('a')+1))