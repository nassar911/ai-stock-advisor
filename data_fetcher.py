import yfinance as yf
import pandas as pd

def get_stock_data(symbol, start=None, end=None):
    data = yf.download(symbol, start=start, end=end, progress=False)
    if data.empty:
        raise ValueError(f"No data found for {symbol}")
    return data
