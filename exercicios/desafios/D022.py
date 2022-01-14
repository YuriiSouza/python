#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao todo (sem considerar espaços);
#Quantas letras tem o primeiro nome;
nome =str(input("Digite o nome: ")).strip()

print(nome.upper())
print(nome.lower())

espacos = nome.count(' ')
ndeLetras = len(nome) - espacos;
print("Número de letras do nome: {}".format(ndeLetras))

lista = nome.split()
ndeLetrasPrimeiro = len(lista[0])
print("Número de letras no primeiro nome: ", ndeLetrasPrimeiro)

#Isso abaixo foi eu complicando o simples...
''''
def ndeLetras( lista, numeroDeTermosDaLista):
    x = 0;
    ndeLetras = 0
    while(numeroDeTermosDaLista <= x):
        ndeLetras = (len(lista[numeroDeTermosDaLista-x])) + ndeLetras;
        x = x + 1;
    
    x = ndeLetras
    return x

n1 = len(lista)

numerodeLetras = ndeLetras(lista, n1)
print("Número de letras do nome é: {}".format(numerodeLetras))
'''