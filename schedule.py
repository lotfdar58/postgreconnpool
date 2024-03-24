import json
from abc import ABC, abstractmethod
from datetime import datetime

from date_range import DateRange


class Schedule(ABC):
    def __init__(self):
        self.date_ranges: list[DateRange] = []

    @abstractmethod
    def get_date_ranges(self, db_connection):
        pass

    def add_range(self, date_range: DateRange):
        self.date_ranges.append(date_range)

    def add_ranges(self, date_ranges: list[DateRange]):
        self.date_ranges = date_ranges

    def get_desired_range(self, utc_date: datetime) -> DateRange:
        Schedule.print_ranges(self.date_ranges, indent=None)
        sorted_ranges = sorted(self.date_ranges, key=lambda date_range: date_range.end_time, reverse=True)
        utc_time_str = utc_date.strftime("%H:%M")
        print(f"UTC time : {utc_date}")
        selected_range = None
        for date_range in sorted_ranges:
            if utc_time_str > date_range.end_time:
                selected_range = date_range
                break
        if selected_range is None:
            selected_range = sorted_ranges[len(sorted_ranges) - 1]

        return selected_range

    @staticmethod
    def print_ranges(date_ranges: list[DateRange], indent: [int, None]):
        json_data = json.dumps([vars(date_range) for date_range in date_ranges], indent=indent)
        print(json_data)


class ScheduleLocal(Schedule):
    def get_date_ranges(self, db_connection):
        range1 = DateRange(1, '01:00', '09:00')
        range2 = DateRange(2, '09:00', '13:00')
        range3 = DateRange(3, '13:00', '20:00')
        range4 = DateRange(4, '20:00', '01:00')
        self.add_ranges([range1, range2, range3, range4])


class ScheduleRemote(Schedule):
    def get_date_ranges(self, db_connection):
        date_ranges = db_connection.get_date_ranges()
        self.add_ranges(date_ranges)
