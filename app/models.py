import datetime

class MonthData(object):

    def __init__(self, month, year, miles, avg_drivers):
        self.month_id = str(month) + '-' + str(year)
        self.month_start = datetime.datetime.strptime(self.month_id, '%m-%Y')
        self.miles = miles
        self.avg_drivers = avg_drivers

    def __repr__(self):
        return '<MONTHDATA {} - {}, {}>'.format(self.month_id, self.miles, self.avg_drivers)
