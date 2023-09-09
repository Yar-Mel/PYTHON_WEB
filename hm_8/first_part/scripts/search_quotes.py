from redis_lru import RedisLRU
from first_part.models import Authors, Quotes
from first_part.connect import create_connection_mongodb, create_connection_redis

redis_client = create_connection_redis()
cache = RedisLRU(redis_client)

connection = create_connection_mongodb()
quotes_collection = Quotes.objects


def search_by_author(author_name):
    author = Authors.objects(fullname__icontains=author_name).first()
    if author:
        quotes = Quotes.objects(author=author)
        result = '\n'.join(quote.quote for quote in quotes)
        return result
    else:
        return "Author not found"


def search_by_tag(tag):
    quotes = Quotes.objects(tags=tag)
    result = '\n'.join(quote.quote for quote in quotes)
    if result:
        return result
    else:
        return "Quotes not found"


def search_by_tags(tags):
    parsed_tags = tags.split(',')
    quotes = Quotes.objects(tags__in=parsed_tags)
    result = '\n'.join(quote.quote for quote in quotes)
    if result:
        return result
    else:
        return "Quotes not found"


def command_parser(input_from_user):
    parsed_data = input_from_user.split(':')
    command, argument = parsed_data[0].strip(), parsed_data[1].strip()
    return command, argument


commands_handler = {
    "name": search_by_author,
    "tag": search_by_tag,
    "tags": search_by_tags
}


if __name__ == "__main__":
    create_connection_mongodb()
    create_connection_redis()

    while True:
        user_input = input("\nInput search command. [Type 'exit' to cancelling]\n>>> ")
        if user_input.lower() != 'exit':
            try:
                command, argument = command_parser(user_input)
            except IndexError:
                print("\nWrong input [Index Error]. Try again\n")
                continue
            if command and argument:
                handler = commands_handler[command]
                result = handler(argument)
                print(result)
            else:
                print("\nWrong input. Try again\n")
        else:
            print("\nGoodbye\n")
            break

