v = 0;
soma = 0;
media = 0;
div = 0;

while v >= 0:
    v = float(input("Digite o valor: "));
    if v >= 0:
        soma = soma + v;
        div = div + 1;

media = soma/div;

print("Quantidade de valores digitados %d" %div);
print("A soma dos valores foi de %.2f" %soma);
print("A media dos valores digitados foi de %.2f" %media);
