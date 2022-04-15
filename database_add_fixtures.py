"""Adding som dummy data to items table"""

import datetime
import sqlite3
from modules.database import Database


def main():
    """insert into table items some dumy data"""
    DB_NAME = 'auto-reminder.sqlite'
    db_connection = sqlite3.connect(DB_NAME)

    items_fixtures_sql = """
    INSERT INTO items (name, email, item_name, return_at) VALUES (?, ?, ?, ?);
    """
    today_date_str = datetime.datetime.now().strftime('%Y-%m-%d') 
    items = [
        ('Janek', 'janek@test.pl', 'milion złotych', today_date_str),
    ]

    with Database(db_connection) as db:
        db.cursor.executemany(items_fixtures_sql, items)


if __name__ == "__main__":
    main()
