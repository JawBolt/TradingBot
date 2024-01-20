
import user_data as UD
import market_data as ms
import buyandsell
import math
import json

running = True

# Algo
#
# check if a bullish candle patturn
# caculate multiple supports and resists (2 peaks within +- 50)
# if all are met buy
# if resistance is met sell
# if price hits support but not bullish patturn then wait 
#for it to hit the support again
# if it doesnt recalculate support and resistance
# 
# Future things to implement
# candle chart patturns 

class create_candle:
  def __init__(self, raw_candle, id):
    self.self = self
    self.raw_candle = raw_candle
    self.id = id
    
  def get_open(self):
    json_candle = json.loads(self.raw_candle)
    return json_candle[int(id)]["o"]

  def get_close(self):
    json_candle = json.loads(self.raw_candle)
    return json_candle[int(id)]["c"]

  def get_id(self):
    return self.id
    
def green_red(open, close, self):
  temp = float(open) - float(close)
  if temp => 0:
    return "red"

  elif temp =< 0:
    return "green"

  else:
    print("An Error Occured!")
    return "err"



def main(API_KEY, SECRET_KEY):
  while running == True:

    
    
