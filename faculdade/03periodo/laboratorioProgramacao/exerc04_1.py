def fac(n):
    if n > 0:
        i = n - 1
        result = n * fac(i)
    else:
        result = 1

    return result


print(fac(5))
