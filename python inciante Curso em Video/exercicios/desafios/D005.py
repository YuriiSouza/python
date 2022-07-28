#Faça um programa que leia um número e retorne seu sucessor e antecessor.
number = int(input("Digite um número: "))

sucussorDeNumber = number + 1;
antecessorDeNumber = number -1;

print("Analisando {} temos\nAntecessor: {}\nSucessor: {}".format(number, antecessorDeNumber, sucussorDeNumber))
#print("Analisando {} temos\nAntecessor: {}\nSucessor: {}".format(number, (number-1), (number+1)))