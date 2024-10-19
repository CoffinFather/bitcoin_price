import requests

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data['bitcoin']['usd']
        return bitcoin_price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

if __name__ == "__main__":
    bitcoin_price = get_bitcoin_price()

    if bitcoin_price is not None:
        print(f"Current Bitcoin Price: ${bitcoin_price}")
