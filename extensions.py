import json
import requests

from config import keys

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        try:
            quote_name = keys[quote]
        except KeyError:
            raise APIException(f'Введена неправильно или несуществующая валюта "{quote}".')

        try:
            base_name = keys[base]
        except KeyError:
            raise APIException(f'Введена неправильно или несуществующая валюта "{base}".')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неправильно введено количество валюты "{amount}".')

        r = requests.get(
            f'https://free.currconv.com/api/v7/convert?q={quote_name}_{base_name}&compact=ultra&apiKey=fa5e1b91ac9d4ca37499')
        total_base = json.loads(r.content)[keys[quote] + '_' + keys[base]]

        return total_base