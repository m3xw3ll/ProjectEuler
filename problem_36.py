cnt = 0

for i in range(1000000):
    if (str(bin(i)[2:]) == str(bin(i)[2:])[::-1]) \
            and str(i) == str(i)[::-1]:
        cnt += i
print(cnt)