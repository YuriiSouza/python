print('''1. Calcular a área de um triângulo;
         2. Ordernar crescente 3 valores;
         3. Ordernar decrescente 3 valores;
         4. Forneça A, B, C para que seja calculado a funçao de segundo grau;
        ''')

choice = int(input("Oque deseja? "))

if choice == 1:
   valueA = float(input('A: '))
   valueB = float(input('B: '))
   valueC = float(input('C: '))
   
   if valueA + valueB > valueC and valueA + valueC > valueB and valueB + valueC > valueA:
        area = (valueA + valueB + valueC) / 2
        print(f'A area do triangulo é {area}')
   else:
        print('Triangulo não existe.')

elif choice == 2:
   valueA = float(input('A: '))
   valueB = float(input('B: '))
   valueC = float(input('C: '))
   
   bigger = valueA
   smaller = valueA
   if valueB >= bigger:
      bigger = valueB;
   if valueB <= smaller:
      smaller = valueB;
   if valueC >= bigger:
      bigger = valueC
   if valueC <= smaller:
      smaller = valueC
      
   if smaller != valueA and bigger != valueA:
      middle = valueA
   if smaller != valueB and bigger != valueB:
      middle = valueB
   else:
      middle = valueC

   print(f'{smaller}, {middle}, {bigger}')
   
elif choice == 3:
   valueA = float(input('A: '))
   valueB = float(input('B: '))
   valueC = float(input('C: '))
        
   bigger = valueA
   smaller = valueA
   if valueB >= bigger:
      bigger = valueB;
   if valueB <= smaller:
      smaller = valueB;
   if valueC >= bigger:
      bigger = valueC
   if valueC <= smaller:
      smaller = valueC
      
   if smaller != valueA and bigger != valueA:
      middle = valueA
   if smaller != valueB and bigger != valueB:
      middle = valueB
   else:
      middle = valueC
      
   print(f'{bigger}, {middle}, {smaller}')
   
else:
   valueA = float(input('A: '))
   valueB = float(input('B: '))
   valueC = float(input('C: '))
   
   delta = (valueB ** 2) - (4 * valueA * valueC)
   
   if delta < 0:
      print('erro')
   elif delta == 0:
      result1 = ((-1 * valueB) + (delta ** 0.5)) / (2 * valueA);
      
      print(f"Valor de x = {result1:.2}")
   else:
      result1 = ((-1 * valueB) + (delta ** 0.5)) / (2 * valueA);
      result2 = ((-1 * valueB) - (delta ** 0.5)) / (2 * valueA);
   
      print(f"Valor de x`= {result1:.2}; x``={result2:.2}")
   