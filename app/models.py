class MonthData(object):

    def __init__(self, month, year, miles, avg_drivers):
        self.month = str(month) + str(year)
        self.miles = miles
        self.avg_drivers = avg_drivers

    def __repr__(self):
        return '<MONTHDATA {} - {}, {}>'.format(self.month, self.miles, self.avg_drivers)
