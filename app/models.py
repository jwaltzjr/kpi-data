import datetime
import pyodbc

from app import db

class MonthData(object):

    @staticmethod
    def fetchall():
        select_statement = """
            SELECT ID, MONTH, MILES, AVG_DRIVERS
            FROM TMWIN.KRC_MONTHLY_KPI_DATA
            WITH UR
        """
        with db as database:
            with database.connection.cursor() as cursor:
                cursor.execute(select_statement)
                return cursor.fetchall()

    @staticmethod
    def fetch(id):
        select_statement = """
            SELECT ID, MONTH, MILES, AVG_DRIVERS
            FROM TMWIN.KRC_MONTHLY_KPI_DATA
            WHERE ID = ?
            WITH UR
        """
        with db as database:
            with database.connection.cursor() as cursor:
                cursor.execute(select_statement, id)
                return cursor.fetchone()

    def __init__(self, month, year, miles, avg_drivers):
        self.month_id = str(month) + '-' + str(year)
        self.month_start = datetime.datetime.strptime(self.month_id, '%m-%Y')
        self.miles = miles
        self.avg_drivers = avg_drivers

    def __repr__(self):
        return '<MONTHDATA {} - {}, {}>'.format(self.month_id, self.miles, self.avg_drivers)

    def insert(self):
        insert_statement = """
            INSERT INTO TMWIN.KRC_MONTHLY_KPI_DATA
                (ID, MONTH, MILES, AVG_DRIVERS)
            VALUES
                (?,?,?,?)
        """
        with db as database:
            with database.connection.cursor() as cursor:
                cursor.execute(
                    insert_statement,
                    self.month_id,
                    self.month_start,
                    self.miles,
                    self.avg_drivers
                )
