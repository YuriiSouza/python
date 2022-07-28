A = int(input("Informe um valor para a variável A: "))
B = int(input("Informe um valor para a variável B: "))

if (A > B):
    aux = A;
    A = B;
    B = aux;
print("O valor da variável A agora é: %i"% A);
print("O valor da variável B agora é: %i"% B);