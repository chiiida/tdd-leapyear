import unittest

from leapyear import LeapYear

test_cases = [
    (False, 1999),
    (True, 2000)
]

def make_leap_year(year):
    return LeapYear(year)

class TestLeapYear(unittest.TestCase):
    def test_Is_Leap_Year(self):
        for testcase in test_cases:
            (isLeapYear, yearInt) = testcase
            year = make_leap_year(yearInt)
            self.assertEqual(isLeapYear, year.is_leap_year())

if __name__ == "__main__":
    unittest.main() 