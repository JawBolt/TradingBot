import hmac
import hashlib
import time
import requests
import json
import simple_colors as color

def sell():
    API_KEY = "ZMYJai18BpGDDnTKJAADTN"
    SECRET_KEY = "MovYm39t5ZMN1nZvHceSc3"

    req = {
        "id": 11,
        "method": "private/create-order",
        "params": {
            "instrument_name": "BTC_USD",
            "side": "SELL",
            "type": "MARKET",
            "quantity": "0.00045",
          },
        "api_key": str(API_KEY),
        "sig": "",
        "nonce": int(time.time() * 1000)
    }

    param_str = ""

    MAX_LEVEL = 3


    def params_to_str(obj, level):
        if level >= MAX_LEVEL:
            return str(obj)

        return_str = ""
        for key in sorted(obj):
            return_str += key
            if obj[key] is None:
                return_str += 'null'
            elif isinstance(obj[key], list):
                for subObj in obj[key]:
                    return_str += params_to_str(subObj, level + 1)
            else:
                return_str += str(obj[key])
        return return_str

    if "params" in req:
        param_str = params_to_str(req['params'], 0)

    payload_str = req['method'] + str(req['id']) + req['api_key'] + param_str + str(req['nonce'])

    req['sig'] = hmac.new(
        bytes(str(SECRET_KEY), 'utf-8'),
        msg=bytes(payload_str, 'utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()

    #print(req)

    sell_response = requests.post("https://api.crypto.com/v2/private/create-order", json=req)
    #print(sell_response)
    #print(sell_response.content)
    print(color.red("SELL"), req["params"]["quantity"], req["params"]["instrument_name"])

def buy():
    
    API_KEY = "ZMYJai18BpGDDnTKJAADTN"
    SECRET_KEY = "MovYm39t5ZMN1nZvHceSc3"

    req = {
        "id": 11,
        "method": "private/create-order",
        "params": {
            "instrument_name": "BTC_USD",
            "side": "BUY",
            "type": "MARKET",
            "quantity": "0.00045"
          },
        "api_key": str(API_KEY),
        "sig": "",
        "nonce": int(time.time() * 1000)
    }

    param_str = ""

    MAX_LEVEL = 3


    def params_to_str(obj, level):
        if level >= MAX_LEVEL:
            return str(obj)

        return_str = ""
        for key in sorted(obj):
            return_str += key
            if obj[key] is None:
                return_str += 'null'
            elif isinstance(obj[key], list):
                for subObj in obj[key]:
                    return_str += params_to_str(subObj, level + 1)
            else:
                return_str += str(obj[key])
        return return_str

    if "params" in req:
        param_str = params_to_str(req['params'], 0)

    payload_str = req['method'] + str(req['id']) + req['api_key'] + param_str + str(req['nonce'])

    req['sig'] = hmac.new(
        bytes(str(SECRET_KEY), 'utf-8'),
        msg=bytes(payload_str, 'utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()

    #print(req)

    sell_response = requests.post("https://api.crypto.com/v2/private/create-order", json=req)
    #print(sell_response)
    #print(sell_response.content)
    print(color.green("BUY"), req["params"]["quantity"], req["params"]["instrument_name"])
    



