def square(number):
    if number not in range(1,65):
        # when the square value is not in the acceptable range        
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    return 2 * square(number-1)


def total():
    total = 0
    for n in range(1, 65):
        total += square(n)
    return total