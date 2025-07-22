import yfinance as yf

def analyze_fundamentals(symbol):
    ticker = yf.Ticker(symbol)
    info = ticker.info

    pe = info.get("trailingPE", None)
    eps = info.get("trailingEps", None)
    roe = info.get("returnOnEquity", None)

    return {
        "pe": pe,
        "eps": eps,
        "roe": roe
    }