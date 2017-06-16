import datetime
from flask_wtf import FlaskForm
from wtforms import DateTimeField, IntegerField, SelectField
from wtforms.validators import DataRequired

MONTHS = [
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December')
]

YEARS = []
for years_ago in range(2):
    year = datetime.datetime.utcnow().year - years_ago
    choice = (str(year), str(year))
    YEARS.append(choice)

class InputForm(FlaskForm):
    month = SelectField(
        'month',
        choices=MONTHS,
        validators=[DataRequired()]
    )
    year = SelectField(
        'year',
        choices=YEARS,
        validators=[DataRequired()]
    )
    miles = IntegerField(
        'miles',
        validators=[DataRequired()]
    )
    avg_drivers = IntegerField(
        'avg_drivers',
        validators=[DataRequired()]
    )
