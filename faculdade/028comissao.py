valor_da_venda = float(input('Valor da venda: '))

if valor_da_venda > 0 and valor_da_venda < 20000:
    print("Comissão R$ 400,00 + 14%. das vendas")
    comissao = (valor_da_venda * 0.14) + 400
    print(f'R$ {comissao:.2f}')
    
elif valor_da_venda >= 20000 and valor_da_venda < 40000:
    print("Comissão R$ 500,00 + 14%. das vendas")
    comissao = (valor_da_venda * 0.14) + 500
    print(f'R$ {comissao:.2f}')

elif valor_da_venda >= 40000 and valor_da_venda < 60000:
    print("Comissão R$ 550,00 + 14%. das vendas")
    comissao = (valor_da_venda * 0.14) + 550
    print(f'R$ {comissao:.2f}')
    
elif valor_da_venda >= 60000 and valor_da_venda < 80000:
    print("Comissão R$ 600,00 + 14%. das vendas")
    comissao = (valor_da_venda * 0.14) + 600
    print(f'R$ {comissao:.2f}')
    
elif valor_da_venda >= 80000 and valor_da_venda < 100000:
    print("Comissão R$ 650,00 + 16%. das vendas")
    comissao = (valor_da_venda * 0.14) + 650
    print(f'R$ {comissao:.2f}')
    
else:
    print("Comissão R$ 700,00 + 16%. das vendas")
    comissao = (valor_da_venda * 0.14) + 400
    print(f'R$ {comissao:.2f}') 
    