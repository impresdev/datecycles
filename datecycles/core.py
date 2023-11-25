from datetime import datetime, timedelta
import calendar
from dateutil.relativedelta import relativedelta


def get_last_day_of_month(year, month):
    """
    Calculate the last day of a specified month and year.

    Args:
        year (int): The year in the Gregorian calendar.
        month (int): The month as an integer, where January is 1 and December is 12.

    Returns:
        datetime: A datetime object representing the last day of the specified month and year.

    Raises:
        TypeError: If the inputs are not integers.
        ValueError: If the month is not in the range 1-12.
    """
    if not isinstance(year, int) or not isinstance(month, int):
        raise TypeError("Year and month must be integers")

    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")

    last_day = calendar.monthrange(year, month)[1]
    return datetime(year, month, last_day)

def add_months(start_date, months):
    """
    Add a specific number of months to a given date.

    Args:
        start_date (datetime): The starting date to which months will be added.
        months (int): The number of months to add to the start_date.

    Returns:
        datetime: A datetime object representing the date after adding the specified number of months.

    Raises:
        TypeError: If start_date is not a datetime object or if months is not an integer.
        ValueError: If the number of months to add is negative.
    """
    if not isinstance(start_date, datetime):
        raise TypeError("start_date must be a datetime object")

    if months < 0:
        raise ValueError("Number of months to add must be non-negative")
    return start_date + relativedelta(months=+months)

def parse_start_date(start_date):
    """
    Parse a string representing a date and return a datetime object. If the day of the month
    is invalid, adjust it to the last valid day of the month.

    Args:
        start_date (str): A string representing a date in 'YYYY-MM-DD' format.

    Returns:
        datetime: A datetime object representing the parsed date.
    """
    try:
        return datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        year, month, _ = map(int, start_date.split('-'))
        return get_last_day_of_month(year, month)

def generate_cycle_dates(start_date, cycle_period, cycle_count):
    """
    Generate a list of dates in a cycle starting from a given date. The function supports various
    cycle periods such as weekly, fortnightly, 4-weekly, monthly, and quarterly.

    Args:
        start_date (str): The starting date of the cycle in 'YYYY-MM-DD' format.
        cycle_period (int): The period of the cycle. Acceptable values are 52 (weekly),
                            26 (fortnightly), 13 (4-weekly), 12 (monthly), and 4 (quarterly).
        cycle_count (int): The number of cycles to generate.

    Returns:
        list: A list of strings where each string is a date in 'YYYY-MM-DD' format, representing the cycle dates.

    Raises:
        TypeError: If the start_date is not a string, or if cycle_period and cycle_count are not integers.
        ValueError: If the cycle count is negative or if the cycle period is not one of the accepted values.
    """
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
