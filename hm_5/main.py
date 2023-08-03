import requests
import aiohttp
import asyncio

from datetime import datetime, timedelta


CURRENCIES = ['EUR', 'USD']


class ApiClient:

    @staticmethod
    async def get_data(url: str):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        print(f'Error status: {response.status}')
            except aiohttp.ClientConnectorError as er:
                print(f'Connection error: {er}')


def get_exchange_rate(data: dict, currencies: list) -> dict:
    result = {}
    for item in data['exchangeRate']:
        for value in item.values():
            if value in currencies:
                result.update(
                    {
                        item['currency']:
                        {
                            'sale': item['saleRateNB'],
                            'purchase': item['purchaseRateNB']
                        }
                    }
                )
    return result


def get_days(number: int) -> list:
    return [(datetime.now() - timedelta(days=i)).strftime("%d.%m.%Y") for i in range(number)]


def main() -> None:
    result_data = []
    while True:
        print("Currencies : EUR, USD. Bank: PB")
        user_input = input("\nEnter days to collect data (max 10). Type 'exit' for cancelling\n>>> ")
        if user_input == "exit":
            break
        else:
            try:
                number_of_days = int(user_input)
            except ValueError:
                print("Wrong input!")
                continue
        if number_of_days > 10:
            print("max days is 10!")
        else:
            days = get_days(number_of_days)
            for day in days:
                data = asyncio.run(ApiClient.get_data(f'https://api.privatbank.ua/p24api/exchange_rates?date={day}'))
                result_data.append({data['date']: get_exchange_rate(data, CURRENCIES)})
            print("Collecting data...")
            print(result_data)
            break


if __name__ == '__main__':
    main()
