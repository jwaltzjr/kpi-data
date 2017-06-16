from flask import Flask

from krc.database import DatabaseConnection
from krc.env import EnvVar

app = Flask(__name__)
app.config.from_object('config')

DATABASE_NAME = 'STALEY'
DATABASE_USER = EnvVar('DBUser').value
DATABASE_PASSWORD = EnvVar('DBPassword').value

db = DatabaseConnection(
    '{IBM DB2 ODBC DRIVER - DB2COPY1}',
    'TM_Reporting_00001',
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD
)

from app import views, models
