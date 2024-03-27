def record(age, gender, wage, childNumber, repetition):

    dataPerson = []

    dataPerson.append(age)
    dataPerson.append(gender)
    dataPerson.append(wage)
    dataPerson.append(childNumber)

    return dataPerson


def avarageWage(data, repetition):
    soma = 0
    p = len(data)
    
    for person in data:
        soma += person[2];
    
    return soma / repetition


def biggerAge(data):
    personAge = []
    for person in data:
        personAge.append(person[0])
    
    biggerAge = max(personAge)
    
    return biggerAge


def smallAge(data):
    personAge = []
    for person in data:
        personAge.append(person[0])
    
    smallAge = min(personAge)
    
    return smallAge

    
def woman(data):
    n = 0
    for person in data:
        if "f" in person[1] and person[3] == 3 and person[2] <= 500:
            n += 1;
    
    return n

    
def main():
    repetition = 15
    data = []
    for n in range(0, repetition):
        print(f"Habitante {n}")

        while True:
            try:
                age = int(input("Idade:"))
                if age < 0:
                    raise ValueError("A idade não pode ser negativa.")
                break
            except ValueError:
                print("Insira uma idade válida.")

        while True:
            gender = input("Gênero: ").strip().lower()
            if gender not in ['masculino', 'feminino', 'outro']:
                print("Insira um gênero válido.")
            else:
                break

        while True:
            try:
                wage = float(input("Salário: "))
                if wage < 0:
                    raise ValueError("O salário não pode ser negativo.")
                break
            except ValueError:
                print("Insira um salário válido.")

        while True:
            try:
                childNumber = int(input("Número de filhos: "))
                if childNumber < 0:
                    raise ValueError("O número de filhos não pode ser negativo.")
                break
            except ValueError:
                print("Insira um número de filhos válido.")

        dataperson = record(age, gender, wage, childNumber, repetition)
        data.append(dataperson)

    media = avarageWage(data, repetition)
    bigger = biggerAge(data)
    small = smallAge(data)
    numberWoman = woman(data)

    print(f'''Média: {media}
          Maior idade: {bigger}
          Menor idade: {small}
          {numberWoman} mulheres recebem até R$ 500,00 e têm 3 filhos
          ''')

main()
