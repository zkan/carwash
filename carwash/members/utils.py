def get_days():
    days = [('', '')]
    for day in range(1, 32):
        days.append((str(day), str(day).zfill(2)))

    return tuple(days)


def get_months():
    months = [('', '')]
    for month in range(1, 13):
        months.append((str(month), str(month).zfill(2)))

    return tuple(months)


def get_years():
    years = [('', '')]
    for year in range(2009, 2055):
        years.append((str(year), str(year)))

    return tuple(years)
