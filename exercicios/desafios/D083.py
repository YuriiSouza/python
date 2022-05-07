#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
analysis1 = 0
analysis2 = 0
formula = str(input("Type it the formula: "))

for n in range(0, len(formula)):
    if '(' == formula[n]:
        analysis1 =+ 1
 
    if ')' == formula[n]:
        analysis2 =+ 1


if analysis1 == analysis2:
    print("the account is white")
else:
    print("The account is wrong")

