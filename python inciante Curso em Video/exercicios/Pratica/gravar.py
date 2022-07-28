n = open('arquivo.txt', 'w')

n.write('Curso Python\n')
n.write('   Coisa linda né....')

n.close()

#----------------

leitura = open('arquivo.txt', 'r')
print(leitura.read())
leitura.close()
