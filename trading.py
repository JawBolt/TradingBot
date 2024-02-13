
import user_data as UD
import market_data as ms
import buyandsell
import math
import json

class create_candle:
    def __init__(self, raw_candle, idNumb):
        self.self = self
        self.raw_candle = raw_candle
        self.idNumb = idNumb

    def get_id(self):
        return str(self.idNumb)
    
    def get_open(self):
        