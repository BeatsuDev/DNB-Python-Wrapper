import dnb

def test_convert():
    conversion = dnb.currency.convert("NOK", "EUR", 50)
    # The converted
    assert conversion < 50

def test_get_conversion_rates():
    conversion_rates = dnb.currency.conversion_rates("NOK")
    # TODO: Add assertion
    assert True
