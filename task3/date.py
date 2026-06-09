def date(year, day):
    if (day <= 31):
        return year, 1, day
    if (day <=  31 + 28):
        return year, 2, day - 31
    if (day <=  31 + 28 + 31):
        return year, 3, day - 31 - 28
    if (day <=  31 + 28 + 31 + 30):
        return year, 4, day - 31 - 28 - 31
    if (day <=  31 + 28 + 31 + 30 + 31):
        return year, 5, day - 31 - 28 - 31 - 30
    if (day <=  31 + 28 + 31 + 30 + 31 + 30):
        return year, 6, day - 31 - 28 - 31 - 30 - 31
    if (day <=  31 + 28 + 31 + 30 + 31 + 30 + 31):
        return year, 7, day - 31 - 28 - 31 - 30 - 31 - 30
    if (day <=  31 + 28 + 31 + 30 + 31 + 30 + 31 + 31):
        return year, 8, day - 31 - 28 - 31 - 30 - 31 - 30 - 31
    if (day <=  31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30):
        return year, 9, day - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31
    if (day <=  31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31):
        return year, 10, day - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31 - 30
    if (day <=  31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30):
        return year, 11, day - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31 - 30 - 31
    return year, 12, day - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31 - 30 - 31 - 30

#DRY violation
#lack of Fail Fast and DWIM we have to verify year and day at least basic verification and adjustment
#lack of leap year validation
#condition complexity smell
#shotgun surgery
#magic numbers
#primitive obsession
