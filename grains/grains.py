# sq  #grain
# 1   1
# 2   2
# 3   4   2(2)
# 4   8 ∑  2(2(2))
# 5   16  2^4
# 6   32  2.2^4
# 5
def square(number):
    if number in range(1, 65):
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


# sum of series in gp,
def total():
    sum = 0
    for i in range(1, 65):
        sum += square(i)
    return sum
