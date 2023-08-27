
from connection import create_connection
from sqlite3 import DatabaseError
from tables_query import CREATE_QUERIES, DROP_QUERIES
from seeds import seeds


def execute_query(connection_to_db, sql_query) -> None:
    try:
        cursor = connection_to_db.cursor()
        cursor.execute(sql_query)
    except DatabaseError as error:
        print(error)


if __name__ == "__main__":
    with create_connection() as connection:
        if connection:
            for query in DROP_QUERIES:
                execute_query(connection, query)
            for query in CREATE_QUERIES:
                execute_query(connection, query)
            # add data to tables
            seeds(connection)
        else:
            print("Connection is None")
