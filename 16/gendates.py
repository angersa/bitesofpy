from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    special_dates = []
    date = PYBITES_BORN
    while date.year < 2020:
        date = date + timedelta(days=100)
        special_dates.append(date)
    date = PYBITES_BORN
    while date.year < 2020:
        date = date + timedelta(days=365)
        special_dates.append(date)
    return sorted(special_dates)


# Much better than mine... Did not follow the instructions well
# (not a generator)
def gen_special_pybites_dates_solution():
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)