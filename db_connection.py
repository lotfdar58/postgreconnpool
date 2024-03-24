import psycopg2
from psycopg2 import pool

from date_range import DateRange


class DbConnection:

    def __init__(self):
        self.connection_pool = DbConnection.db_connection_pool()

    @staticmethod
    def db_connection_pool():
        try:
            connection_pool = psycopg2.pool.SimpleConnectionPool(1, 2,
                                                                 user="postgres",
                                                                 password="",
                                                                 host="",
                                                                 port="5432",
                                                                 database="postgres"
                                                                 )
            if connection_pool:
                print("Connection pool created successfully")
                return connection_pool
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)

    def close_pull_connection(self):
        if self.connection_pool:
            self.connection_pool.closeall()
        print("Threaded PostgreSQL connection pool is closed")

    def get_date_ranges(self):
        ranges: list[DateRange] = []
        ps_connection = None
        try:
            ps_connection = self.connection_pool.getconn()
            with ps_connection.cursor() as cursor:
                cursor.execute("select * from date_range")
                rows = cursor.fetchall()
                for row in rows:
                    id, start_time, end_time = row
                    start_time_str = start_time.strftime("%H:%M")
                    end_time_str = end_time.strftime("%H:%M")
                    ranges.append(DateRange(id, start_time_str, end_time_str))
        except Exception as err:
            print(err)
        finally:
            if ps_connection:
                self.connection_pool.putconn(ps_connection)
            return ranges
