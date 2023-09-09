import json
from pathlib import Path

from first_part.models import Authors, Quotes
from first_part.connect import create_connection_mongodb

connection = create_connection_mongodb()

file_path = Path(__file__).parent.parent.joinpath("json/quotes.json")


def quotes_json(path):
    with open(path, "r") as quotes_file:
        quotes_data = json.load(quotes_file)
        for quote_data in quotes_data:
            author_name = quote_data["author"]
            author = Authors.objects(fullname=author_name).first()
            if author:
                quote_data["author"] = author
                Quotes(**quote_data).save()


if __name__ == "__main__":
    quotes_json(file_path)
