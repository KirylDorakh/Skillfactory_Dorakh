import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты: {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {quote}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
        total = json.loads(r.content)['rates'][base_ticker]
        return total

    @staticmethod
    def get_price(message):
        try:
            values = message.text.lower().split(' ')
            if len(values) != 3:
                raise APIException('Неверное количество параметров')
            quote, base, amount = values
            total = CryptoConverter.convert(quote, base, amount)
        except APIException as e:
            text = f'Ошибка пользователя\n{e}'
        except Exception as e:
            text = f'Не удалось обработать запрос\n{e}'
        else:
            text = f"Актуальный курс: {amount} {keys[quote]} = {total * float(amount)} {keys[base]}"
        return text
