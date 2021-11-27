import requests
import keys
import pandas as pd
from time import sleep

def get_crypto_rates(base_currency='USD', assets='BTC, ETH, XRP' ):
    url = 'https://api.nomics.com/v1/currencies/ticker'

    payload = {'key' : keys.NOMICS_API_KEY, 'convert': base_currency, 'ids': assets 'interval': 'id'}
    response = requests.get(url, params=payload)
    data = response.json()

    crypto_currency, cypto_price,crypto_timespace = [], [], []

    