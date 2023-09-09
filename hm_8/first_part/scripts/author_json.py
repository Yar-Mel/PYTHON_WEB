import json
from pathlib import Path

from first_part.models import Authors
from first_part.connect import create_connection_mongodb

connection = create_connection_mongodb()

file_path = Path(__file__).parent.parent.joinpath("json/authors.json")


def author_file_json(path):
    with open(path, "r") as authors_file:
        authors_data = json.load(authors_file)
        for author_data in authors_data:
            Authors(**author_data).save()


if __name__ == "__main__":
    author_file_json(file_path)
