from stuf import stuf

api = "https://developer-api.dnb.no/"
test_api = "https://developer-api-testmode.dnb.no/"

currency_endpoints = stuf(
    conversion_rates="currencies/v1/convert/{quote_currency}",
    conversion="currencies/v1/{base_currency}/convert/{quote_currency}"
)