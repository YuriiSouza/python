#Faça um programa que leia os catetos e retorne a hipotenusa.
import math

Cadjacente = float(input("Comprimento do cateto adjacente: "))
Coposto = float(input("Comprimento do cateto oposto: "))

hipotenusa = math.hypot(Cadjacente,Coposto);
#hipotenusa = (((Coposto**2)+(Cadjacente**2)))**(1/2);

print("A hipotenusa tem comprimento de {}.".format(hipotenusa))
