#Faça um programa que leia um valor em graus e retorne o valor do seno cosseno e tangente.
from math import radians, sin, cos, tan
angulo = float(input("Digite o valor do ângulo: "))

sen = sin(radians(angulo));
coss = cos(radians(angulo));
tg = tan(radians(angulo));

print("SENO: {:.1f}\nCOSSENO: {:.1f}\nTANGENTE: {:.1f}".format(sen, coss, tg))