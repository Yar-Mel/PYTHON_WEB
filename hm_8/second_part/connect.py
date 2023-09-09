import configparser
import pika
from pathlib import Path
from colorama import init, Fore
from mongoengine import connect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

init(autoreset=True)

file_config = Path(__file__).parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

mongo_user = config.get('mongodb', 'user')
mongodb_pass = config.get('mongodb', 'pass')
db_name = config.get('mongodb', 'db_name')
domain = config.get('mongodb', 'domain')

rabbitmq_host = config.get("rabbitmq", "rabbitmq_host")
rabbitmq_port = config.get("rabbitmq", "rabbitmq_port")
rabbitmq_username = config.get("rabbitmq", "rabbitmq_username")
rabbitmq_password = config.get("rabbitmq", "rabbitmq_password")


def create_connection_mongodb():
    url = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority"
    conn = connect(host=url, alias='default')
    return conn


def create_connection_rabbitmq():
    connection_params = pika.ConnectionParameters(
        host=rabbitmq_host, port=rabbitmq_port,
        credentials=pika.PlainCredentials(username=rabbitmq_username, password=rabbitmq_password)
    )
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    return channel, connection


def check_mongodb_connection():
    try:
        host = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority"
        client = MongoClient(host, server_api=ServerApi('1'))

        print(Fore.YELLOW + f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority")

        if client.admin.command('ping'):
            print(Fore.GREEN + "Connected to MongoDB successful!")
        else:
            print(Fore.RED + "Connection failed")
    except Exception as e:
        print(Fore.RED + "Connection error:", e)


def check_rabbitmq_connection(rabbitmq_host, rabbitmq_port, rabbitmq_username, rabbitmq_password):
    try:
        credentials = pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
        parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)

        connection = pika.BlockingConnection(parameters)
        connection.close()

        print(Fore.GREEN + "Connected to RabbitMQ successful!")
        return True
    except pika.exceptions.AMQPConnectionError:
        print(Fore.RED + "Connection to RabbitMQ failed")
        return False


if __name__ == "__main__":
    create_connection_mongodb()
    rabbitmq_channel, rabbitmq_connection = create_connection_rabbitmq()

    check_mongodb_connection()
    check_rabbitmq_connection(rabbitmq_host, rabbitmq_port, rabbitmq_username, rabbitmq_password)
