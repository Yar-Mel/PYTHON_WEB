import scrapy
import json

from scrapy.crawler import CrawlerProcess
from scrapy.item import Item, Field

from itemadapter import ItemAdapter


class QuoteItem(Item):
    tags = Field()
    author = Field()
    quote = Field()


class AuthorItem(Item):
    fullname = Field()
    description = Field()
    born_date = Field()
    born_location = Field()


class QuotesPipeline:
    quotes = []
    authors = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if "fullname" in adapter.keys():
            self.authors.append(
                {
                    "fullname": adapter["fullname"],
                    "description": adapter["description"],
                    "born_date": adapter["born_date"],
                    "born_location": adapter["born_location"],
                }
            )
        elif "quote" in adapter.keys():
            self.quotes.append(
                {
                    "tags": adapter["tags"],
                    "author": adapter["author"],
                    "quote": adapter["quote"],
                }
            )
        return "Process success"

    def close_spider(self, spider):
        with open("quotes.json", "w", encoding="UTF-8") as fd:
            json.dump(self.quotes, fd, ensure_ascii=False)
        with open("authors.json", "w", encoding="UTF-8") as fd:
            json.dump(self.authors, fd, ensure_ascii=False)


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]
    custom_settings = {"ITEM_PIPELINES": {QuotesPipeline: 10}}

    def parse(self, response, *args):

        def parse_quotes(field):
            tags = field.xpath("div[@class='tags']/a/text()").extract()
            author = field.xpath("span/small/text()").get()
            quote = field.xpath("span[@class='text']/text()").get()
            return QuoteItem(
                tags=tags,
                author=author,
                quote=quote
            )

        def parse_authors(author_response):
            field = author_response.xpath("/html//div[@class='author-details']")
            fullname = field.xpath("h3[@class='author-title']/text()").get()
            description = field.xpath("div[@class='author-description']/text()").get().strip().replace('\"', '')
            born_date = field.xpath("p/span[@class='author-born-date']/text()").get()
            born_location = field.xpath("p/span[@class='author-born-location']/text()").get()
            return AuthorItem(
                fullname=fullname,
                description=description,
                born_date=born_date,
                born_location=born_location
            )

        for quote_field in response.xpath("/html//div[@class='quote']"):
            yield parse_quotes(quote_field)
            yield response.follow(
                url=self.start_urls[0] + quote_field.xpath("span/a/@href").get(),
                callback=parse_authors
            )

        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()
