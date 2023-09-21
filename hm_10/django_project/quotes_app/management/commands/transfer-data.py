import pymongo
from datetime import datetime
from django.core.management.base import BaseCommand
from quotes_app.models import Authors, Quotes


class Command(BaseCommand):
    help = "Transfer data from MongoDB to Postgres"

    def handle(self, *args, **options):
        try:
            # Connect to MongoDB
            mongo_client = pymongo.MongoClient(
                "mongodb+srv://admin:admin@pythonweb.cuxtlft.mongodb.net/"
            )

            # Select MongoDB database and collections
            mongo_db = mongo_client["QuotesToScrape"]
            mongo_authors = mongo_db["authors"]
            mongo_quotes = mongo_db["quotes"]

            # Loop through MongoDB data and transfer to Postgres
            for mongo_author in mongo_authors.find():
                author = Authors.objects.create(
                    fullname=mongo_author["fullname"],
                    born_date=datetime.strptime(mongo_author["born_date"], "%B %d, %Y"),
                    born_location=mongo_author["born_location"],
                    description=mongo_author["description"],
                )

                self.stdout.write(
                    self.style.SUCCESS('Data "Author" transfer completed successfully.')
                )

                for mongo_quote in mongo_quotes.find({"author": mongo_author["_id"]}):
                    try:
                        Quotes.objects.create(
                            tags=mongo_quote["tags"],
                            author=author,
                            quote=mongo_quote["quote"],
                        )

                        self.stdout.write(
                            self.style.SUCCESS(
                                'Data "Quote" transfer completed successfully.'
                            )
                        )

                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(f"Error inserting quote: {e}")
                        )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
