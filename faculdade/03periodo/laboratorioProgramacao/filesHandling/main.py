file = open("data.txt", "w")

number = 10
file.write(str(number))

file.close()

file = open("data.txt", "r")

text = file.read()

print(text)