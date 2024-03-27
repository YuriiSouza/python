import random

def biggerthenZero(data):
  n = 0
  for number in data:
    if number > 0:
      n += 1

  return n


def smallerthenZero(data):
  n = 0
  for number in data:
    if number < 0:
      n += 1;

  return n


def main():
  list = []
  for n in range(0, 30):
    randomNumber = random.randint(-100, 100)
    list.append(randomNumber)

  positive = biggerthenZero(list)
  negative = smallerthenZero(list)

  print(f'''
          Na lista {list}, existem: 
          {positive} numeros maiores que zero
          {negative} numeros menores que zero
        ''')
  
main()