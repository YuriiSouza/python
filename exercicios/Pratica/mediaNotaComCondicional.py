n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

média = (n1+n2)/2;

print("Média final: {}".format(média))

if média > 6.0:
    print("APROVADO")
else:
    print("REPROVADO")

#print("APROVADO" if média > 6.0 else"REPROVADO")

print('='*20)