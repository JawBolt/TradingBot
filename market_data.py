
import requests
import json
   
def last_candles(count, symbol):
    request = requests.get("https://api.crypto.com/exchange/v1/public/get-candlestick?instrument_name=" + str(symbol) + "&timeframe=5m&count=" + str(count))
    content = request.content
    json_content = json.loads(content)
    return json_content["result"]["data"]
    # 0 is newest and <count> is oldest

def coin_price(symbol):
    latest_candle = last_candles(1, str(symbol))
    return latest_candle[0]["c"]

