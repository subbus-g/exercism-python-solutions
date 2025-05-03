def equilateral(sides):
    return sides != [0, 0, 0] and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    a, b, c = sides
    return (
        sides != [0, 0, 0]
        and (a + b >= c and b + c >= a and c + a >= b)
        and (a == b or b == c or c == a)
    )


def scalene(sides):
    a, b, c = sides
    return (
        sides != [0, 0, 0]
        and (a + b >= c and b + c >= a and c + a >= b)
        and (a != b != c != a) 
    )
