def invert(n):
    if n == 0:
        return n
    else:
        print(n % 10)
        
        n = n // 10
        return invert(n)


print(invert(123))
