from math import radians, sin, cos, tan
angulo = float(input("Digite o valor do ângulo: "))

sen = sin(radians(angulo));
cos = cos(radians(angulo));
tg = tan(radians(angulo));

print("SENO: {:.1f}\nCOSSENO: {:.1f}\nTANGENTE: {:.1f}".format(sen, cos, tg))