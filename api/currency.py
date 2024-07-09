import requests


def get_currency():
    base_url = 'https://v6.exchangerate-api.com/v6/09edf8b2bb246e1f801cbfba/latest/USD'
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        return data
    except:
        return None



