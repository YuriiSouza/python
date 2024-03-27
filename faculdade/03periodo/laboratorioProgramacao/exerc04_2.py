def fib(n):
    if n > 0:
        nFib = fib(n-1) + fib(n-2)
        n = n - 1
    else:
        nFib = 1
        
    return nFib
    
print(fib(0))
