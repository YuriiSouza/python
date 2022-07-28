#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input("Digite o número que deseja ver a tabuada: "))

for c in range(1,11):
    print(f"{n:2} X {c:2} = {(c * n):2}")
