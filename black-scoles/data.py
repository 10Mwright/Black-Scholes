import yfinance as yf

def getTicker(tickerSymbol):
    print("Getting ticker: ", tickerSymbol)

    return yf.Ticker(tickerSymbol)