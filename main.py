import requests
import keys
import pandas as pd
from time import sleep

def get_crypto_rates(base_currency='USD', assets='BTC, ETH, XRP' ):
    url = 'https://api.nomics.com/v1/currencies/ticker'

    payload = {'key': keys.NOMICS_API_KEY, 'convert': base_currency, 'ids': assets, 'interval': 'id'}
    response = requests.get(url, params=payload)
    data = response.json()

    crypto_currency, crypto_price,crypto_timestamp = [], [], []
    
    for asset in data:
        crypto_currency.append(asset['currency'])
        crypto_price.append(asset['price'])
        crypto_timestamp.append(asset['price_timestamp'])
    
    raw_data = {
        'assets' : crypto_currency,
        'rates' : crypto_price,
        'timestamp' : crypto_timestamp

    }

    df = pd.DataFrame(raw_data)
    print(df)
    return df


get_crypto_rates('ZAR', 'DOT')