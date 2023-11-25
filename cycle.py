from datetime import datetime, timedelta
import calendar
from dateutil.relativedelta import relativedelta


def get_last_day_of_month(year, month):
    last_day = calendar.monthrange(year, month)[1]
    return datetime(year, month, last_day)

def add_months(start_date, months):
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
    if cycle_count < 0:
        raise ValueError("Cycle count must be non-negative")

    start_date_obj = parse_start_date(start_date)

    cycle_dates = []

    for i in range(cycle_count):
        if cycle_period == 52:  # Weekly cycles
            cycle_date = start_date_obj + timedelta(weeks=1 * i)
        elif cycle_period == 26:  # Fortnightly cycles
            cycle_date = start_date_obj + timedelta(weeks=2 * i)
        elif cycle_period == 13:  # 4-weekly cycles
            cycle_date = start_date_obj + timedelta(weeks=4 * i)
        elif cycle_period == 12:  # Monthly cycles
            cycle_date = add_months(start_date_obj, i)
        elif cycle_period == 4:  # Quarterly cycles
            cycle_date = add_months(start_date_obj, 3 * i)
        else:
            raise ValueError("Invalid cycle period")

        cycle_dates.append(cycle_date.strftime("%Y-%m-%d"))

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
