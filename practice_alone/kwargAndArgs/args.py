def multiply(*args):
    multiply_args = 1
    while True:
        try:    
            for elements_of_args in args:
                multiply_args *= elements_of_args
            break
        except:
            print("ERRO")

    return multiply_args


print(multiply(9, 5, 1, 3, 4))
