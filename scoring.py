def get_final_score(technical, financial):
    tech_score = 0
    if technical['sma_bullish']:
        tech_score += 1
    if technical['macd_signal']:
        tech_score += 1
    if technical['rsi'] < 30:
        tech_score += 1
    elif technical['rsi'] > 70:
        tech_score -= 1

    fin_score = 0
    if financial['pe'] and financial['pe'] < 20:
        fin_score += 1
    if financial['eps'] and financial['eps'] > 0:
        fin_score += 1
    if financial['roe'] an...