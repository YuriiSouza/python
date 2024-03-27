#Questão Desafio
# Um feirante possui uma balança de dois pratos e um contrapeso W ∈ N da forma 1
# 2 (3n+1 −1)|n ∈
# N para pesar itens em sua loja. Nesta situação inicial, ele consegue pesar apenas itens de peso
# W , uma vez que se os dois pratos se balanceiam significa que o conteúdo do outro prato tem o
# mesmo peso do contrapeso. Infelizmente o contrapeso utilizado pelo feirante cai no chão e se
# parte em n pedaços distintos da forma (estou sendo propositalmente vago) ∑n
# i=1 wi = W ∈ N.
# Miraculosamente, o feirante percebeu que com aqueles novos pedaços, não só ele conseguiria
# pesar itens de peso W , mas todos os itens no intervalo de peso [1, ..., W ], através do correto
# balanceamento dos pedaços entre os dois pratos da balança.
# Escreva um algoritmo que, dado um peso W , compute os n subpesos do feirante e exiba a
# configuração de pesos na balança para pesar todos os pesos inteiros de 1 até W .
# O programa terá as seguintes características:
# • Escrito em linguagem C;
# • O valor do peso W será lido através de um argumento passado através do parâmetro argv,
# a saída do programa será realizada em um arquivo de texto (extensão txt)
# • A saída do programa será realizada em um arquivo de texto com o nome “resultado.txt”,
# de tal forma que cada linha do arquivo de texto terá a forma: x = p1 ± p2 ± p3 ± ... ± pn
# onde x é um peso no intervalo [1, ..., W ] e p1 ±p2 ±p3 ±...±pn são os subpesos computados
# à partir do peso inicial W .
# • Não haverá qualquer outro conteúdo neste arquivo de texto além do mencionado assim
# O relatório deverá:
# • Explicar o funcionamento do algoritmo;
# • Conter detalhes comentados da implementação;
# • Expor fontes de pesquisa utilizadas para realização do trabalho.
# Esta é uma questão bônus valendo um ponto na média final da disciplina de APC-1 nas
# turmas de Engenharia de Produção e Engenharia de Minas. Grupos de até 5 pessoas podem ser
# autores de uma solução, esta deve ser submetida ao email luisvinicius ufcat.edu.br até o dia
# 09/02/2024, e a apresentação da solução deve ser realizada até o dia 16/02/2024, em formato
# de seminário durante a aula. Apenas o primeiro grupo/autor das duas turmas como um todo
# que solucionar o problema receberá a pontuação extra.