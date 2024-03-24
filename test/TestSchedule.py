import unittest
from datetime import datetime, timezone

from date_range import DateRange
from schedule import Schedule


class TestSchedule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        range1 = DateRange(1, '01:00', '09:00')
        range2 = DateRange(2, '09:00', '13:00')
        range3 = DateRange(3, '13:00', '20:00')
        range4 = DateRange(4, '20:00', '01:00')
        cls.ranges = [range1, range2, range3, range4]

    def test_get_desired_range_1(self):
        expected = self.ranges[3]
        utc_date = datetime(2024, 3, 24, 1, 30)
        schedule = Schedule()
        schedule.date_ranges = self.ranges
        actual = schedule.get_desired_range(utc_date)
        self.assertEqual(vars(actual), vars(expected))

    def test_get_desired_range_2(self):
        expected = self.ranges[1]
        utc_date = datetime(2024, 3, 24, 14, 30)
        schedule = Schedule()
        schedule.date_ranges = self.ranges
        actual = schedule.get_desired_range(utc_date)
        self.assertEqual(vars(actual), vars(expected))

    def test_get_desired_range_3(self):
        expected = self.ranges[3    ]
        utc_date = datetime(2024, 3, 24, 2, 30)
        schedule = Schedule()
        schedule.date_ranges = self.ranges
        actual = schedule.get_desired_range(utc_date)
        self.assertEqual(vars(actual), vars(expected))
