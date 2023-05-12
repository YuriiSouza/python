n = int(input())
arr = map(int, input().split())

biggerNumber = 0
second_place = 0

for points in arr:
    if biggerNumber == 0:
        biggerNumber = points
    elif points > biggerNumber:
        biggerNumber = points
    
for points in arr:
    if points > second_place:
        n = second_place
        second_place = points
        if second_place == biggerNumber:
            second_place = n
        

print(second_place)
print(biggerNumber)
