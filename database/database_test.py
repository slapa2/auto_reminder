import sqlite3
from datetime import datetime
from collections import namedtuple
import pytest
from .database import Database


@pytest.fixture
def create_connection_and_db():
    """
    create connection to database with table and fixture data
    """
    create_items_table_sql = """CREATE TABLE items (
	id integer primary key autoincrement,
	name text not null,
	email text not null,
	item_name text not null,
	return_at date not null
);"""
    today_date_str = datetime.now().strftime('%Y-%m-%d')

    insert_sql = """INSERT INTO items (name, email, item_name, return_at) values (?, ?, ?, ?);"""
    sample_data = [
        ('Jan', 'jan@mail.pl', 'item 1', today_date_str),
        ('Anna', 'anna@mail.pl', 'item 2', '2000-01-01'),
        ('Tom', 'tom@mail.pl', 'item 3', '2050-01-01'),
    ]

    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute(create_items_table_sql)
    cursor.executemany(insert_sql, sample_data)

    return connection


def test_get_all_rows(create_connection_and_db):
    """
    Test db connecion get all rows
    """
    with Database(create_connection_and_db) as db:
        data = db.get_all_rows('select * from items;', tuple())

    assert len(data) == 3

def test_get_one_row(create_connection_and_db):
    """
    Test db connection get one row
    """
    today = datetime.now().strftime('%Y-%m-%d')
    with Database(create_connection_and_db) as db:
        data = db.get_row(
            'select * from items where return_at = ?;',
            [today]
        )

    assert data.name == 'Jan'
    assert data.email == 'jan@mail.pl'
    assert data.item_name == 'item 1'
    assert data.return_at == today
    
    
    