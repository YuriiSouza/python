codigo = int(input("Codigo: "))
nome = str(input("Qual o nome do funcionario?  "))
salario = float(input("Qual o valor do salário? "))
ativo = bool(input("Qual o valor do ativo? 0 ou 1  "))

print("O código: %d" % codigo)
print("O nome: %s" % nome)
print("Valor do salário: %d" % salario)
print("Valor do ativo em: %r" % ativo)