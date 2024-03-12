import sys
import numpy as np

import data

def main():
    tickerSymbol = sys.argv[1]

    ticker = data.getTicker(tickerSymbol)

    print(ticker)

    calculate(54, 53, 0.2, 5, 0.2) ## TEMP ##

def calculate(currentPrice, strikePrice, rfInterestRate, time, volatility):
    
    d1 = (np.emath.logn(strikePrice, currentPrice) + (rfInterestRate + ((np.square([volatility]) / 2) * time))) / volatility * np.sqrt(time)
    
    d2 = d1 - volatility * np.sqrt(time)

    nDistributionD1 = np.random.normal(d1, 1, 1) # TODO: Review ##
    nDistributionD2 = np.random.normal(d2, 1, 1) # TODO: Review ##

    optionPrice = (currentPrice * nDistributionD1 * d1) - strikePrice * np.exp(-rfInterestRate*time) * nDistributionD2 * d2

    print("Black-Scholes value is: ", optionPrice)

    return optionPrice

main()