import os

from date_range import DateRange
from db_connection import DbConnection
from schedule import ScheduleRemote, ScheduleLocal
from datetime import datetime, timezone


def main():
    print('application is running...')

    db_connection = None
    try:
        schedule = None
        is_local = bool(os.environ.get('LOCAL', False))
        if is_local:
            schedule = ScheduleLocal()
        else:
            db_connection = DbConnection()
            schedule = ScheduleRemote()

        schedule.get_date_ranges(db_connection)

        utc_date = datetime.now(timezone.utc)
        desired_range = schedule.get_desired_range(utc_date)
        print(f"Desired range:  {desired_range}")
    except Exception as error:
        print(error)
    finally:
        db_connection.close_pull_connection()


if __name__ == '__main__':
    main()
