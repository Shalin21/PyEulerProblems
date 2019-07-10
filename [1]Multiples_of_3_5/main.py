total = 0
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        total += num
print(total)

print(sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0))
