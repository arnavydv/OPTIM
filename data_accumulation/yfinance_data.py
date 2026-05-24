import yfinance as yf
import pandas as pd 
data=yf.Ticker('AAPL')

aapl_historical = data.history(start="2023-05-23", end="2026-05-23", interval="1d")
"""so this aapl_historical ticker is a pandas dataframe so 
we are going to use pandas here"""
final_data=aapl_historical.to_csv("C:\\Users\\Admin\\Desktop\\FBSDE PROJECT\\data_accumulation\\aapl_data.csv")
print(type(final_data))