import yfinance as yf
import pandas as pd 
data=yf.Ticker('AAPL')

aapl_historical = data.history(start="2025-06-02", end="2025-06-07", interval="1h")
"""so this aapl_historical ticker is a pandas dataframe so 
we are going to use pandas here"""
aapl_historical['Close']