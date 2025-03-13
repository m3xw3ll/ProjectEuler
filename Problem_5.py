check_list = [11, 13, 14, 16, 17, 18, 19, 20]

for num in range(20, 999999999, 20):
    if all(num % n == 0 for n in check_list):
        print(num)
        break
