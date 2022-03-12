lanche = 'hamburgue','suco','pizza','pudim'

#for comida in range(0, len(lanche)):
   # print(f"Irie comer {lanche[c]}")

for comida in enumerate(lanche):
    print(f"Irie comer {comida}")
'''
#for comida in lanche:
    print(f"Irie comer {comida}")
'''
'''''
print(sorted(lanche))

#a = 1, 2, 3
#b = 4, 5
#c = a + b
print(c)#somar em tupla adiciona os elementos de uma na outra  
print(len(c))#quantidade de termos em "c"
print(c.count(2))#quantas vezes aparecem 2 na tupla "c"
print(c.index(3))
print(c.index(4, 0))#leitura feita a partir do termo no indice 0

pessoa = 'Yuri', 18, 'masculino'
del(pessoa)
print(pessoa)
'''