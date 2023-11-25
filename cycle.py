from datetime import datetime, timedelta
import calendar
from dateutil.relativedelta import relativedelta


def get_last_day_of_month(year, month):
    if not isinstance(year, int) or not isinstance(month, int):
        raise TypeError("Year and month must be integers")

    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")

    last_day = calendar.monthrange(year, month)[1]
    return datetime(year, month, last_day)

def add_months(start_date, months):
    if not isinstance(start_date, datetime):
        raise TypeError("start_date must be a datetime object")

    if months < 0:
        raise ValueError("Number of months to add must be non-negative")
    return start_date + relativedelta(months=+months)

def parse_start_date(start_date):
    """Parse and validate the start date."""
    try:
        return datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        year, month, _ = map(int, start_date.split('-'))
        return get_last_day_of_month(year, month)

def generate_cycle_dates(start_date, cycle_period, cycle_count):
    if not isinstance(start_date, str):
        raise TypeError("start_date must be a string")

    if not isinstance(cycle_period, int) or not isinstance(cycle_count, int):
        raise TypeError("cycle_period and cycle_count must be integers")

    if cycle_count < 0:
        raise ValueError("Cycle count must be non-negative")

    start_date_obj = parse_start_date(start_date)

    cycle_strategies = {
        52: lambda d, i: d + timedelta(weeks=i),
        26: lambda d, i: d + timedelta(weeks=2 * i),
        13: lambda d, i: d + timedelta(weeks=4 * i),
        12: lambda d, i: add_months(d, i),
        4: lambda d, i: add_months(d, 3 * i)
    }

    if cycle_period not in cycle_strategies:
        raise ValueError("Invalid cycle period")

    cycle_dates = [cycle_strategies[cycle_period](start_date_obj, i).strftime("%Y-%m-%d") for i in range(cycle_count)]

    return cycle_dates

# Example usage
print(generate_cycle_dates("2023-10-01", 12, 3))  # monthly for 3 cycles
print(generate_cycle_dates("2023-10-01", 13, 3))  # 4-weekly for 3 cycles
print(generate_cycle_dates("2023-10-01", 26, 6))  # fortnightly for 6 cycles
print(generate_cycle_dates("2023-10-01", 52, 6))  # weekly for 6 cycles
print(generate_cycle_dates("2023-02-29", 12, 4))  # Adjusts to correct last day of Feb
print(generate_cycle_dates("2023-11-32", 12, 5))  # Adjusts to last day of month

# ['2023-10-01', '2023-11-01', '2023-12-01']
# ['2023-10-01', '2023-10-29', '2023-11-26']
# ['2023-10-01', '2023-10-15', '2023-10-29', '2023-11-12', '2023-11-26', '2023-12-10']
# ['2023-10-01', '2023-10-08', '2023-10-15', '2023-10-22', '2023-10-29', '2023-11-05']
# ['2023-02-28', '2023-03-28', '2023-04-28', '2023-05-28']
# ['2023-11-30', '2023-12-30', '2024-01-30', '2024-02-29', '2024-03-30']
