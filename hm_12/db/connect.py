import psycopg2
import os
import configparser
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

current_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = os.path.join(current_directory, "connect.ini")

if os.path.exists(config_file_path):
    config = configparser.ConfigParser()
    config.read(config_file_path)

    db_config = config["DB"]
    db_user = db_config["USER"]
    db_password = db_config["PASSWORD"]
    db_name = db_config["NAME"]
    db_host = db_config["HOST"]
    db_port = db_config["PORT"]
else:
    print("Wrong path")

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_database_connection():
    return psycopg2.connect(
        host="localhost",
        database="db-postgres",
        user="postgres",
        password="567234",
    )


def execute_query(query, params=None):
    conn = get_database_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
