from app.models import MonthData
from app import DATABASE_USER, DATABASE_PASSWORD

print(DATABASE_USER)
print(DATABASE_PASSWORD)
test_month = MonthData('04','2017',10000,65)
test_month.save()
