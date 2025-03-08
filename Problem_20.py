fact = 1
for i in range(1, 101):
    fact *= i

print(sum(int(num) for num in str(fact)))