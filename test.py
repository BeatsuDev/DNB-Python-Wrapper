# API key set in .env if run with pipenv. Alternatively, set it here:
# import os
# os.environ["APIKEY"] = "<your-api-key>"

# You can also set whether to use the live api or the sandbox api:
# os.environ["LIVE"] = "True"

import dnb.currency.conversion

conversion = dnb.currency.conversion.convert("NOK", "EUR", 50)
print(conversion)

print('\n\n---------------------------------\n\n')

conversion_rates = dnb.currency.conversion.conversion_rates("NOK")
print(conversion_rates)