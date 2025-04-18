import armstrong_numbers_test


def is_armstrong_number(number):
    # s=str(number)
    # # l = len(str(number))
    # sum=0
    # for c in s:
    #     sum += int(c) ** len(s)
    # return sum == number
    digits = []
    number_copy = number
    while(number_copy):
        last_digit = number_copy % 10
        digits.append(last_digit)
        number_copy //= 10
    sum =0
    for digit in digits:
        sum += digit ** len(digits)
    return sum == number