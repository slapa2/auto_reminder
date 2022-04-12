"""Adding som dummy data to items table"""

import sqlite3
from database.database import Database


def main():
    """insert into table items some dumy data"""
    DB_NAME = 'auto-reminder.db'
    db_connection = sqlite3.connect(DB_NAME)

    items_fixtures_sql = """
    INSERT INTO items (name, email, item_name, return_at) VALUES (?, ?, ?, ?);
    """
    items = [
        ('Janek', 'janek@test.pl', 'milion złotych', '2022-04-12'),
    ]

    with Database(db_connection) as db:
        db.cursor.executemany(items_fixtures_sql, items)


if __name__ == "__main__":
    main()
