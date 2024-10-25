def steps(number):
    if number<=0 :
     # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")
    steps = int()
    while number != 1:
        # if n is even
        if not number % 2:
            number /= 2
        else:
            number = 3 * number + 1
        steps+=1
    return steps
