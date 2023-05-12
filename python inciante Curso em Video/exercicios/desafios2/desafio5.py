from math import inf


n = int(input())
arr = map(int, input().split())

biggerNumber = (-inf)
second_place = (-inf)

for points in arr:
    if points > biggerNumber:
        second_place = biggerNumber
        biggerNumber = points
    elif points > second_place and points != biggerNumber:
        second_place = points
    


print(second_place)
print(biggerNumber)
