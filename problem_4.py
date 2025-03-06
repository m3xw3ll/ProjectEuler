# https://projecteuler.net/problem=4

out = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if str(i * j) == str(i * j)[::-1]:
            out = max(out, i*j)
print(out)