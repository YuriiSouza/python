def Sum(n):

    sum = 0
    
    for i in range(1, n+1):
        sum += ((i**2) + 1) / (i + 3)
        
    return sum

repetionTimes = int(input("Type a number: "))

print(Sum(repetionTimes))
