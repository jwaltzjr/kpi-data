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
    'STALEY',
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD,
    hostname='10.10.81.19',
    port='50000'
)

from app import views, models
