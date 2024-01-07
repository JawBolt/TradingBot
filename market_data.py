
import requests
import json

def latest_btc():
    Lbtc_request = requests.get("https://api.crypto.com/exchange/v1/public/get-candlestick?instrument_name=BTC_USD&timeframe=5m")
    Bcontent = Lbtc_request.content
    json_BTC = json.loads(Bcontent)
    Latest_BTC_price = jsonP["result"]["data"][24]["c"]
    return Latest_BTC_price   
    
def last_candles(count, symbol):
    request = requests.get("https://api.crypto.com/exchange/v1/public/get-candlestick?instrument_name=" + str(symbol) + "&timeframe=5m&count=" + str(count))
    content = request.content
    json_content = json.loads(content)
    return json_content["result"]["data"]


def latest_sol():
    Lsol_request = requests.get("https://api.crypto.com/exchange/v1/public/get-candlestick?instrument_name=SOL_USD&timeframe=5m")
    Scontent = Lsol_request.content
    json_sol = json.loads(Scontent)
    Latest_SOL_price = json_sol["result"]["data"][24]["c"]
    return Latest_SOL_price


