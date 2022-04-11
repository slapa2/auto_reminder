"""
Databased auto reminder program
"""

import os
import datetime
import dotenv
from database.database import DatabaseConnector
from mailer.mailer import Mailer

dotenv.load_dotenv()
DB_PATH = os.getenv('DB_PATH')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
USERNAME = os.getenv('USERNAME')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
USE_SSL = bool(int(os.getenv('USE_SSL')))

database = DatabaseConnector(DB_PATH)
mailer = Mailer(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD, USE_SSL)

today_remindes = database.get_all_rows(
    'select * from items where return_at = ?',
    [datetime.datetime.now().strftime('%Y-%m-%d')]
)

for remind in today_remindes:
    mailer.send(
        mail_from=EMAIL,
        mail_to=remind.email,
        subject=f'przypomnienie o zrocie {remind.item_name}',
        message=f'Hej {remind.name}, najwyzsza pora zebys oddal/a mi {remind.item_name}!'
    )
