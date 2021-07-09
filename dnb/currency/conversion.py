import os, json, re
import requests
import stuf
import arrow

from ..endpoints import api, test_api, currency_endpoints



def conversion_rates(currency, apikey = os.environ.get("APIKEY"), live = os.environ.get("LIVE", False)):
    url = api if live else test_api
    url += currency_endpoints.conversion_rates.format(quote_currency=currency)

    resp = requests.get(
        url, headers={"x-api-key": apikey}
    )
    return json.loads(resp.content)

def convert(fro, to, amt, apikey = os.environ.get("APIKEY"), live=os.environ.get("LIVE", False)):
    url = api if live else test_api
    url += currency_endpoints.conversion.format(base_currency=fro, quote_currency=to)

    resp = requests.get( 
        url, params={"amount": amt}, headers={"x-api-key": apikey}
    )
    return Conversion(json.loads(resp.content))



class Conversion(stuf.stuf):
    '''Contains information associated a conversion. 
    Supports basic operators and assumes mid rate convesion'''
    def __init__(self, conversion_data):
        # Convert camelCase to snake_case (insert _ before every upper case letter,
        # then conver to lowercase)
        self.data = {re.sub(r"([A-Z])", r"_\1", k).lower():v for k,v in conversion_data.items()}
        self.__all__ = list(self.data.keys())
        super().__init__(self.data)

    # Arithmetic
    def __add__(self, other):
        return self.mid_rate+other
    def __sub__(self, other):
        return self.mid_rate-other
    def __mul__(self, other):
        return self.mid_rate*other
    def __floordiv__(self, other):
        return self.mid_rate//other
    def __truediv__(self, other):
        return self.mid_rate/other
    
    # Comparison
    def __lt__(self, other):
        return self.mid_rate<other
    def __le__(self, other):
        return self.mid_rate<=other
    def __eq__(self, other):
        return self.mid_rate == other
    def __ne__(self, other):
        return self.mid_rate != other
    def __gt__(self, other):
        return self.mid_rate>other
    def __ge__(self, other):
        return self.mid_rate>=other

    # Other
    def __round__(self, decimals):
        return round(self.mid_rate, decimals)