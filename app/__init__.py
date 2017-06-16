from flask import Flask

from ..krc.database import DatabaseConnection
from ..krc.env import EnvVar

app = Flask(__name__)
app.config.from_object('config')

DATABASE_NAME = 'STALEY'
db = DatabaseConnection(
    '{IBM DB2 ODBC DRIVER - DB2COPY1}',
    'TM_Reporting_00001',
    DATABASE_NAME,
    EnvVar('DBUser').value,
    EnvVar('DBPassword').value
)

from app import views, models
