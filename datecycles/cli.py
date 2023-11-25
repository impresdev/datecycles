#!/usr/bin/env python
import argparse
from datetime import datetime
from datecycles.core import generate_cycle_dates

def main():
    parser = argparse.ArgumentParser(description="Generate a series of dates based on a cycle period.")
    parser.add_argument("start_date", type=str, help="Start date in YYYY-MM-DD format")
    parser.add_argument("cycle_period", type=int, choices=[52, 26, 13, 12, 4], help="Cycle period (52, 26, 13, 12, 4)")
    parser.add_argument("cycle_count", type=int, help="Number of cycles to generate")

    args = parser.parse_args()

    try:
        # Ensure the start date is in the correct format
        datetime.strptime(args.start_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Start date must be in YYYY-MM-DD format")

    cycle_dates = generate_cycle_dates(args.start_date, args.cycle_period, args.cycle_count)
    for date in cycle_dates:
        print(date)

if __name__ == '__main__':
    main()
