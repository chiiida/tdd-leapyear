import pytest

from leapyear_unittest import test_cases, make_leap_year

class TestLeapYear:

    @pytest.mark.parametrize('isLeapYear YearInt'.split(), test_cases)
    def test_get_score(self, isLeapYear, YearInt):
        year = make_leap_year(YearInt)
        assert isLeapYear == year.is_leap_year()