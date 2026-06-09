import unittest
from date import date
from date_refactored import DateRefactored


class TestDate(unittest.TestCase):
    def test_date(self):
        self.assertEqual(date(2023, 1), (2023, 1, 1))
        self.assertEqual(date(2023, 60), (2023, 3, 1))
        self.assertEqual(date(2023, 256), (2023, 9, 13))
        self.assertEqual(date(2023, 365), (2023, 12, 31))

        self.assertEqual(DateRefactored.create(2023, 1).to_tuple(), (2023, 1, 1))
        self.assertEqual(DateRefactored.create(2023, 60).to_tuple(), (2023, 3, 1))
        self.assertEqual(DateRefactored.create(2023, 256).to_tuple(), (2023, 9, 13))
        self.assertEqual(DateRefactored.create(2023, 365).to_tuple(), (2023, 12, 31))

if __name__ == '__main__':
    unittest.main()
