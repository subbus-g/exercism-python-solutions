def leap_year(year):
    # # if the year is a century year
    # if year % 100 == 0:
    #     return year % 400 == 0
    # # if the year is not a century year
    # else:
    #     return year % 4 == 0

    # year must be divisble by 4 and
    # year must not be a century unless it is a centory
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)