import itertools

s = input(int())

groups = itertools.groupby(s)

print(groups[1])
