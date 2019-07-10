first = 1
second = 2
num = first + second
finalSum = 2
while num < 4000000:
    first = second
    second = num
    num = first + second
    if num % 2 == 0:
        finalSum += num
print(finalSum)