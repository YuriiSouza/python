#Faça um programa que leia um valor inteiro, calcule e retorne a raiz quadrada, triplo e dobro do valor inserido.
number = int(input("Digite um valor: "))

#raizQuadradaNumber = number**(1/2);
raizQuadradaNumber = pow(number, (1/2));
triploNumber = number*3;
dobroNumber = number*2;

#print("O dobro do valor {}: {}\nO triplo do valor {} é: {}\nA raiz quadrada de {} é: {:.2f}".format(number, (number*2), number, (number*3), number, (number**(1/2))))

print("O dobro do valor {}: {}\nO triplo do valor {} é: {}\nA raiz quadrada de {} é: {}".format(number, dobroNumber, number, triploNumber, number, raizQuadradaNumber))