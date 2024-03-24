import json


class DateRange:

    def __init__(self, id, start_time, end_time):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        json_data = json.dumps(vars(self))
        return json_data

