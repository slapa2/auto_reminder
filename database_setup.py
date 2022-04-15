"""create database and table items"""

import sqlite3
from modules.database import Database


def main ():
    """creating database and table items"""
    DB_NAME = 'auto-reminder.sqlite'
    db_connection = sqlite3.connect(DB_NAME)

    create_items_table_sql = """CREATE TABLE items (
	id integer primary key autoincrement,
	name text not null,
	email text not null,
	item_name text not null,
	return_at date not null
);"""

    with Database(db_connection) as db:
        db.cursor.execute(create_items_table_sql, tuple())


if __name__ == "__main__":
    main()
