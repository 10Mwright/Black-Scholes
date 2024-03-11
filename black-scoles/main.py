import sys
import yfinance as yf

import data

def main():
    tickerSymbol = sys.argv[1]

    ticker = data.getTicker(tickerSymbol)

    print(ticker)

main()