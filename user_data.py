import hmac
import hashlib
import time
import requests
import json
import ast

def user_balence(API_KEY, SECRET_KEY):

    req = {
        "id": "11",
        "method": "private/user-balance",
        "params": {},
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

    user_bal = requests.post("https://api.crypto.com/exchange/v1/private/user-balance", json=req)
    content = user_bal.content
    dict_str = content.decode('utf-8')
    json_bal = json.loads(dict_str)
    return json_bal["result"]["data"][0]["total_cash_balance"]
