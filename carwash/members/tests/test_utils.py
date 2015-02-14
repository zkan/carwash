from django.test import TestCase

from ..utils import get_days, get_months, get_years


class MemberUtilsTest(TestCase):
    def test_get_days_should_return_tuple_of_one_to_thirty(self):
        days = [('', '')]
        for day in range(1, 32):
            days.append((str(day), str(day).zfill(2)))

        expected = tuple(days)
        actual = get_days()

        self.assertEqual(actual, expected)

    def test_get_months_should_return_tuple_of_one_to_twelve(self):
        months = [('', '')]
        for month in range(1, 13):
            months.append((str(month), str(month).zfill(2)))

        expected = tuple(months)
        actual = get_months()

        self.assertEqual(actual, expected)

    def test_get_years_should_return_tuple_of_2010_to_2055(self):
        years = [('', '')]
        for year in range(2009, 2055):
            years.append((str(year), str(year)))

        expected = tuple(years)
        actual = get_years()

        self.assertEqual(actual, expected)
