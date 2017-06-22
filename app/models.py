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
                queryset = cursor.fetchall()
        months = []
        for row in queryset:
            month = MonthData(
                row.MILES,
                row.AVG_DRIVERS,
                month_id=row.ID
            )
            months.append(month)
        return months

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
                month = cursor.fetchone()
        return MonthData(
            month.MILES,
            month.AVG_DRIVERS,
            month_id=month.ID
        )

    def __init__(self, miles, avg_drivers, month=None, year=None, month_id=None):
        if (month and year):
            self.month_id = str(month) + '-' + str(year)
        elif month_id:
            self.month_id = month_id
        else:
            raise ValueError('Missing arguments - no month provided.')
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

    def update(self):
        update_statement = """
            UPDATE TMWIN.KRC_MONTHLY_KPI_DATA
            SET MILES = ?, AVG_DRIVERS = ?
            WHERE ID = ?
        """
        with db as database:
            with database.connection.cursor() as cursor:
                cursor.execute(
                    update_statement,
                    self.miles,
                    self.avg_drivers,
                    self.month_id
                )
