
import sqlite3
import typing
from contextlib import contextmanager


@contextmanager
def create_connection() -> typing.Generator:
    connection = None
    try:
        connection = sqlite3.connect("hm_6.db")
        yield connection
        connection.commit()
    except Exception as error:
        print(error)
        connection.rollback()
    finally:
        connection.close()
