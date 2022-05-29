from stuf import stuf

import dnb.currency

__version__ = "0.0.1"
API_ENDPOINT = "https://developer-api.dnb.no"
TEST_ENDPOINT = "https://developer-api-testmode.dnb.no"

currency_endpoints = stuf(
    conversion_rates="currencies/v1/convert/{quote_currency}",
    conversion="currencies/v1/{base_currency}/convert/{quote_currency}"
)