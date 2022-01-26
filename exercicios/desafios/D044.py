#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
tipoDePagamento = str(input('''O pagamento será em:
1. À vista dinheiro/cheque:10%' de desconto
2. À vista no cartão: 5%' de desconto
3. Em até 2x no cartão: preço formal
4. 3x ou mais no cartão: 20%' de juros\n''')).lower()
preco = float(input("Valor do produto: "))

if tipoDePagamento == '1' or tipoDePagamento == 'dinheiro' or tipoDePagamento == 'cheque':
    preco = preco - (preco * 0.1);
    print("O valor será R${:.2f}. 10%' de DESCONTO".format(preco))
elif tipoDePagamento == '2':
    preco = preco - (preco * 0.05);
    print("Valor será de R${:.2f}. 5%' de DESCONTO".format(preco))
elif tipoDePagamento == '3' or tipoDePagamento == '2x no cartão':
    print("O valor se mantém em R${:.2f}. SEM JUROS".format(preco))
elif tipoDePagamento == '4':
    preco = preco + (preco * 0.2);
    nParcelas = int(input("Número de parcelas: "))
    vParcela = preco/nParcelas;
    print("Valor do produto R${:.2f}, pago em {} a R${:.2f}. COM 20%' DE JUROS".format(preco, nParcelas, vParcela))
else:
    print("ERRO")
