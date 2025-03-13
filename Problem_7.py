cnt = 0
p = 2

while cnt <= 10001:
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        cnt += 1
    if cnt == 10001:
        print(p)
    else:
        p += 1