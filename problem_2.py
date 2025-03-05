# https://projecteuler.net/problem=2

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

i = 1
j = 1
s = 0
while j <= 4000000:
    j = fib(i)
    if j % 2 == 0:
        s += j
    i += 1
print(s)