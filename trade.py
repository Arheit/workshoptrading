#MACD Workshop 

import sys
import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
plt.style.use('fivethirtyeight')

from google.colab import files

upload = files.upload()

# store in Dataframe 

df = pd.read_csv('AAPL.csv')

df = df.set_index(pd.DatetimeIndex(df['Date'].values))

#MACD 

ShortEMA = df.Close.ewm(span=12, adjust=False).mean()
LongEMA = df.Close.ewm(span=26, adjust=False).mean()

MACD = ShortEMA - LongEMA
signal = MACD.ewm(span=9, adjust=False).mean()

plt.figure(figsize=(12.2, 4.5))
plt.plot(df.index, MACD, label = 'APPL MACD', color='red')
plt.plot(df.index, signal, label='sig line', color='blue')
plt.show()

df['MACD'] = MACD 
df['signal'] = signal

def buy_and_sell(signal, flag):
  for i in range(0, len(signal)):
    if signal['MACD'][i] > signal['signal']:
      if flag != 1:
        print("Buy")
        flag =  1
    if signal['MACD'][i] > signal['signal']:
      if flag != 1:
        print("SELL")
        flag =  1