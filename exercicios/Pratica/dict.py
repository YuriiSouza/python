dados = {'nome':'Joao', 'idade': 23}

print(dados)

#adicionando um indice com um valor ao dicionário
dados["sexo"] = "m"

print(dados)
print(dados.values())
print(dados.keys())
print(dados.items())

dadoscopia = dados.copy()
