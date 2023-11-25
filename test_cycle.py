import unittest
from cycle import get_last_day_of_month, add_months, generate_cycle_dates
from datetime import datetime

class DateCycleTest(unittest.TestCase):

    def test_get_last_day_of_month(self):
        self.assertEqual(get_last_day_of_month(2023, 1), datetime(2023, 1, 31))
        self.assertEqual(get_last_day_of_month(2023, 2), datetime(2023, 2, 28))
        self.assertEqual(get_last_day_of_month(2024, 2), datetime(2024, 2, 29))  # Leap year

    def test_add_months(self):
        self.assertEqual(add_months(datetime(2023, 1, 30), 1), datetime(2023, 2, 28))
        self.assertEqual(add_months(datetime(2023, 11, 30), 2), datetime(2024, 1, 30))

    def test_monthly_cycle(self):
        self.assertEqual(generate_cycle_dates("2023-10-01", 12, 3), ['2023-10-01', '2023-11-01', '2023-12-01'])

    def test_four_weekly_cycle(self):
        self.assertEqual(generate_cycle_dates("2023-10-01", 13, 3), ['2023-10-01', '2023-10-29', '2023-11-26'])

    def test_fortnightly_cycle(self):
        self.assertEqual(generate_cycle_dates("2023-10-01", 26, 6), ['2023-10-01', '2023-10-15', '2023-10-29', '2023-11-12', '2023-11-26', '2023-12-10'])

    def test_weekly_cycle(self):
        self.assertEqual(generate_cycle_dates("2023-10-01", 52, 6), ['2023-10-01', '2023-10-08', '2023-10-15', '2023-10-22', '2023-10-29', '2023-11-05'])

    def test_adjust_date_for_invalid_day(self):
        self.assertEqual(generate_cycle_dates("2023-02-29", 12, 4), ['2023-02-28', '2023-03-28', '2023-04-28', '2023-05-28'])

    def test_adjust_date_for_invalid_month_day(self):
        self.assertEqual(generate_cycle_dates("2023-11-32", 12, 4), ['2023-11-30', '2023-12-30', '2024-01-30', '2024-02-29'])

    # Add any other tests for generate_cycle_dates function or other functions as needed

if __name__ == '__main__':
    unittest.main()
