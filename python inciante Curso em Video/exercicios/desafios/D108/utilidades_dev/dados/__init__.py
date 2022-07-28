def price_validation(value):
    value.strip()
    while True:
        if value == '' or value.isnumeric() == False:
            print("ERROR")
        else:
            break
    value = value.replace(',', '.')

    return value
    