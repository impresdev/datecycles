import unittest
from cycle import get_last_day_of_month, add_months, generate_cycle_dates
from datetime import datetime

class TestCycleModule(unittest.TestCase):

    # Tests for get_last_day_of_month
    def test_get_last_day_regular_month(self):
        self.assertEqual(get_last_day_of_month(2023, 1), datetime(2023, 1, 31))

    def test_get_last_day_february_non_leap_year(self):
        self.assertEqual(get_last_day_of_month(2023, 2), datetime(2023, 2, 28))

    def test_get_last_day_february_leap_year(self):
        self.assertEqual(get_last_day_of_month(2024, 2), datetime(2024, 2, 29))

    def test_get_last_day_invalid_month(self):
        with self.assertRaises(ValueError):
            get_last_day_of_month(2023, 0)

    def test_get_last_day_invalid_month_high(self):
        with self.assertRaises(ValueError):
            get_last_day_of_month(2023, 13)

    def test_get_last_day_invalid_year(self):
        with self.assertRaises(ValueError):
            get_last_day_of_month(-1, 2)


    # Tests for add_months
    def test_add_months_zero_month(self):
        self.assertEqual(add_months(datetime(2023, 1, 15), 0), datetime(2023, 1, 15))

    def test_add_months_normal(self):
        self.assertEqual(add_months(datetime(2023, 1, 15), 1), datetime(2023, 2, 15))

    def test_add_months_year_rollover(self):
        self.assertEqual(add_months(datetime(2023, 12, 15), 1), datetime(2024, 1, 15))

    def test_add_months_negative(self):
        with self.assertRaises(ValueError):
            add_months(datetime(2023, 1, 15), -1)

    def test_add_months_large_number(self):
        self.assertEqual(add_months(datetime(2023, 1, 15), 120), datetime(2033, 1, 15))


    # Tests for generate_cycle_dates
    def test_generate_cycle_monthly(self):
        expected_dates = ['2023-10-01', '2023-11-01', '2023-12-01']
        self.assertEqual(generate_cycle_dates("2023-10-01", 12, 3), expected_dates)

    def test_generate_cycle_four_weekly(self):
        expected_dates = ['2023-10-01', '2023-10-29', '2023-11-26']
        self.assertEqual(generate_cycle_dates("2023-10-01", 13, 3), expected_dates)

    def test_generate_cycle_fortnightly(self):
        expected_dates = ['2023-10-01', '2023-10-15', '2023-10-29', '2023-11-12', '2023-11-26', '2023-12-10']
        self.assertEqual(generate_cycle_dates("2023-10-01", 26, 6), expected_dates)

    def test_generate_cycle_weekly(self):
        expected_dates = ['2023-10-01', '2023-10-08', '2023-10-15', '2023-10-22', '2023-10-29', '2023-11-05']
        self.assertEqual(generate_cycle_dates("2023-10-01", 52, 6), expected_dates)

    def test_generate_cycle_last_day_of_february(self):
        expected_dates = ['2023-02-28', '2023-03-28', '2023-04-28', '2023-05-28']
        self.assertEqual(generate_cycle_dates("2023-02-29", 12, 4), expected_dates)

    def test_generate_cycle_adjust_last_day_of_month(self):
        expected_dates = ['2023-11-30', '2023-12-30', '2024-01-30', '2024-02-29', '2024-03-30']
        self.assertEqual(generate_cycle_dates("2023-11-32", 12, 5), expected_dates)

    def test_generate_cycle_invalid_cycle_period(self):
        with self.assertRaises(ValueError):
            generate_cycle_dates("2023-01-01", 5, 2)

    def test_generate_cycle_invalid_date_format(self):
        with self.assertRaises(ValueError):
            generate_cycle_dates("2023-13-01", 12, 3)

    def test_generate_cycle_negative_cycle_count(self):
        with self.assertRaises(ValueError):
            generate_cycle_dates("2023-01-01", 12, -1)


if __name__ == '__main__':
    unittest.main()
