import datetime
from flask_wtf import FlaskForm
from wtforms import DateTimeField, IntegerField, SelectField
from wtforms.validators import DataRequired

MONTHS = [
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December')
]

class InputForm(FlaskForm):
    month = SelectField(
        'month',
        choices=MONTHS,
        validators=[DataRequired()]
    )
    year = IntegerField(
        'year',
        default=int(datetime.datetime.utcnow().year),
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
