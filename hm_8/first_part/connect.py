import configparser
import redis
from pathlib import Path
from colorama import init, Fore
from mongoengine import connect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from redis_lru import RedisLRU

init(autoreset=True)

file_config = Path(__file__).parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

mongo_user = config.get('mongodb', 'user')
mongodb_pass = config.get('mongodb', 'pass')
db_name = config.get('mongodb', 'db_name')
domain = config.get('mongodb', 'domain')

redis_host = config.get('redis', 'redis.host')
redis_port = config.get('redis', 'redis_port')


def create_connection_mongodb():
    url = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority"
    conn = connect(host=url, alias='default')
    return conn


def create_connection_redis():
    redis_client = redis.StrictRedis(host="localhost", port=6379, password=None)
    cache = RedisLRU(redis_client)
    return cache


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


def check_redis_connection(host, port):
    try:
        redis_client = redis.StrictRedis(host=host, port=port)
        redis_client.ping()
        if redis_client.ping():
            print(Fore.GREEN + "Connected to Redis successful!")
            return True
        else:
            print(Fore.RED + "Connected to Redis, but ping failed")
            return False
    except redis.ConnectionError:
        print(Fore.RED + "Connection to Redis failed")
        return False


if __name__ == "__main__":
    create_connection_mongodb()
    create_connection_redis()

    check_mongodb_connection()
    check_redis_connection(redis_host, redis_port)
