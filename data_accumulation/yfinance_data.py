import yfinance as yf
data=yf.Ticker('AAPL')

aapl_historical = data.history(start="2025-06-02", end="2025-06-07", interval="1h")
print(aapl_historical)