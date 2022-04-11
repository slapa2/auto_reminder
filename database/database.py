"""sqlite database connection module"""

import sqlite3
from typing import List, Tuple, NamedTuple
from collections import namedtuple


class Database:
    """Database connector"""
    def __init__(self, connection) -> None:
        self.connection = connection
        self.cursor = None

    def __enter__(self):
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def get_all_rows(self, sql: str, bindings: Tuple) -> List[NamedTuple]:
        """
        query data from database and return results as a list of named tuples
        """

        self.cursor.execute(sql, bindings)
        rows = self.cursor.fetchall()
        print(rows)
        return [self._to_named_tuple(row) for row in rows]

    def get_row(self, sql: str, bindings: Tuple) -> NamedTuple:
        """
        query a data from database and return first row as named tuple
        """
        self.cursor.execute(sql, bindings)
        return self._to_named_tuple(self.cursor.fetchone())

    @staticmethod
    def _to_named_tuple(row: sqlite3.Row) -> NamedTuple:
        """
        return named tuple based on Row object
        """
        Row = namedtuple('Row', row.keys())
        return Row(*tuple(row))
