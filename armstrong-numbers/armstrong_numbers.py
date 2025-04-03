def is_armstrong_number(number):
    s=str(number)
    # l = len(str(number))
    sum=0
    for c in s:
        sum += int(c) ** len(s)
    return sum == number
    
is_armstrong_number(153)