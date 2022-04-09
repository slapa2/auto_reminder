"""module provides connection to sqlite database"""

import sqlite3
from typing import List, Tuple, NamedTuple
from collections import namedtuple


DB_NAME = 'sqlite3.db'


class DatabaseContextManager:
    """connection to database context manager"""
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = sqlite3.Row
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.connection.close()


class DatabaseConnector:
    """sqlite3 database connector calss"""

    def __init__(self, db_name) -> None:
        self.db_name = db_name

    def get_all_rows(self, sql: str, bindings: Tuple) -> List[NamedTuple]:
        """
        query data from database and return results as a list of named tuples
        """
        with DatabaseContextManager(self.db_name) as cur:
            cur.execute(sql, bindings)
            rows = cur.fetchall()
        return [self._to_named_tuple(row) for row in rows]

    def get_row(self, sql: str, bindings: Tuple) -> NamedTuple:
        """
        query a data from database and return first row as named tuple
        """
        with DatabaseContextManager(self.db_name) as cur:
            cur.execute(sql, bindings)
            row = cur.fetchone()
        return self._to_named_tuple(row)

    @staticmethod
    def _to_named_tuple(row: sqlite3.Row) -> NamedTuple:
        """
        return named tuple based on Row object
        """
        Row = namedtuple('Row', row.keys())
        return Row(*tuple(row))
