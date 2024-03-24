from date_range import DateRange
from db_connection import DbConnection
from schedule import Schedule
from datetime import datetime, timezone


def main():
    print('application is running...')
    # range1 = DateRange(1, '01:00', '09:00')
    # range2 = DateRange(2, '09:00', '13:00')
    # range3 = DateRange(3, '13:00', '20:00')
    # range4 = DateRange(4, '20:00', '01:00')

    db_connection = None
    try:
        db_connection = DbConnection()
        date_ranges = db_connection.get_date_ranges()
        schedule = Schedule()
        schedule.add_ranges(date_ranges)

        utc_date = datetime.now(timezone.utc)
        desired_range = schedule.get_desired_range(utc_date)
        print(f"Desired range:  {desired_range}")
    except Exception as error:
        print(error)
    finally:
        db_connection.close_pull_connection()


if __name__ == '__main__':
    main()
