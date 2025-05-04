def leap_year(year):
    # if the year is a century year
    if year % 100 == 0:
        return year % 400 == 0
    # if the year is not a century year
    else:
        return year % 4 == 0
