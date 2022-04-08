import os
import dotenv
from database.db import DatabaseConnector
from mailer.mailer import Mailer


def main():

    dotenv.load_dotenv()
    DB_PATH = os.getenv('DB_PATH')
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMPT_PORT = int(os.getenv('SMTP_PORT'))
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    
    db = DatabaseConnector(DB_PATH)
    mailer = Mailer(SMTP_SERVER, SMPT_PORT, EMAIL, PASSWORD)


if __name__ == '__main__':
    main()