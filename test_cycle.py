import unittest
from datetime import datetime, timedelta
from cycle import get_last_day_of_month, add_months, generate_cycle_dates

class DateCycleTest(unittest.TestCase):

    def test_get_last_day_of_month(self):
        self.assertEqual(get_last_day_of_month(2023, 1), datetime(2023, 1, 31))
        self.assertEqual(get_last_day_of_month(2023, 2), datetime(2023, 2, 28))
        self.assertEqual(get_last_day_of_month(2024, 2), datetime(2024, 2, 29))  # Leap year

    def test_add_months(self):
        self.assertEqual(add_months(datetime(2023, 1, 30), 1), datetime(2023, 2, 28))
        self.assertEqual(add_months(datetime(2023, 11, 30), 2), datetime(2024, 1, 30))

    def test_generate_cycle_dates(self):
        self.assertEqual(generate_cycle_dates("2023-10-01", 12, 3), ['2023-10-01', '2023-11-01', '2023-12-01'])
        self.assertEqual(generate_cycle_dates("2023-02-29", 12, 4), ['2023-02-28', '2023-03-28', '2023-04-28', '2023-05-28'])

        with self.assertRaises(ValueError):
            generate_cycle_dates("2023-10-01", 7, 3)  # Invalid cycle period

if __name__ == '__main__':
    unittest.main()
