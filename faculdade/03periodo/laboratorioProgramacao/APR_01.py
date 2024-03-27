def ret(number):
    if number > 0:
        return 1
    else:
        return 0
    
def main():
    number = int(input("Number: "))
    print(ret(number))
    
if __name__ == '__main__':
    main()
    