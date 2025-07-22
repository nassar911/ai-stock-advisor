from data_fetcher import get_stock_data
from technical_analysis import analyze_technicals
from financial_analysis import analyze_fundamentals
from scoring import get_final_score
import pandas as pd

def backtest(symbol, start_date, end_date):
    df = get_stock_data(symbol, start=start_date, end=end_date)
    df['Signal'] = None
    df['BuyPrice'] = None
    df['SellPrice'] = None
    position = False
    buy_price = 0
    returns = []

    for i in range(50, len(df)):
        ...