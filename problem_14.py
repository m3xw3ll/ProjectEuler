def collatz(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = (x*3) + 1
    return collatz(y) + 1


print(str(max(range(1, 1000000), key=collatz)))