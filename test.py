import os

import dnb.currency.conversion

os.environ["APIKEY"] = "test"
print(os.environ.get("APIKEY", "nothin"))

conversion = dnb.currency.conversion.convert("NOK", "EUR", 50)
print(conversion)