import time
import json
from data_fetcher import get_stock_data
from technical_analysis import analyze_technicals
from financial_analysis import analyze_fundamentals
from scoring import get_final_score
from notifier import send_email, send_telegram

# Load config from config.json
with open("config.json") as f:
    config = json.load(f)

WATCHLIST = config.get("watchlist", ["AAPL", "AMZN", "TSLA"])
INTERVAL_MINUTES = config.get("interval_minutes", 5)

# Store last action per stock to reduce redundant alerts
last_actions = {}

def run_analysis():
    print("\n================= LIVE ANALYSIS =================")
    for symbol in WATCHLIST:
        try:
            print(f"\nAnalyzing {symbol}...")
            df = get_stock_data(symbol)
            technical_result = analyze_technicals(df)
            financial_result = analyze_fundamentals(symbol)
            final = get_final_score(technical_result, financial_result)

            print(f"Symbol: {symbol}")
            print(f"Signal: {final['action']}")
            print(f"Score: {final['score']:.2f}")
            if final['price_range']:
                print(f"Recommended Price Range: {final['price_range'][0]} - {final['price_range'][1]}")

            # Send alert if action has changed
            previous_action = last_actions.get(symbol)
            if final['action'] != previous_action:
                last_actions[symbol] = final['action']
                subject = f"Trading Alert for {symbol}: {final['action']}"
                message = (
                    f"Signal: {final['action']}\n"
                    f"Score: {final['score']:.2f}\n"
                    + (
                        f"Price Range: {final['price_range'][0]} - {final['price_range'][1]}"
                        if final['price_range']
                        else ""
                    )
                )
                send_email(subject, message)
                send_telegram(f"{subject}\n{message}")

        except Exception as e:
            print(f"Error analyzing {symbol}: {e}")

if __name__ == '__main__':
    while True:
        run_analysis()
        print(f"\nWaiting {INTERVAL_MINUTES} minutes...")
        time.sleep(INTERVAL_MINUTES * 60)
