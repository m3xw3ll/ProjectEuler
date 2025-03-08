seq = range(1, 101)
sum_squares = sum(i**2 for i in seq)
square_sum = sum(seq)**2
print(square_sum - sum_squares)