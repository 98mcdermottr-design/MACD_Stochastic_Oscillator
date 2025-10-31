# trading_strategy_backtest.py

import yfinance as yf          # To download historical stock data
import pandas as pd            # For data manipulation (tables, calculations)
import numpy as np             # For numerical calculations (mean, std, etc.)
import matplotlib.pyplot as plt # For plotting charts

def download_data(ticker, start, end):
    """Download historical data from Yahoo Finance""" #called docstring, like comment at beginning of function but doesn't affect code
# 3 quotations means you can write multi-line strings
    data = yf.download(ticker, start=start, end=end)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]
    return data

def MACD_Signal(data, short_window=50, long_window=200, signal_window=14):
    """Generates MACD and Signal line"""
    # ewm is the exponential weighted moving function, when used in conjection to .mean()
    # you then get the exponential moving average, which gives larger weights in the mean
    # calculation to more recent prices, which makes sense as this a momentum and technical indicator
    data['EMA_short'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA_long'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA_short'] - data['EMA_long']
    data['Signal'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    data['Histogram'] = data['MACD'] - data['Signal']
    return data

# Parameters
# Ask for user inputs
ticker = input("Enter ticker (e.g. AAPL, MSFT, TSLA): ").upper()
start = input("Enter start date (YYYY-MM-DD): ")
end = input("Enter end date (YYYY-MM-DD): ")

# Run pipeline
data = download_data(ticker, start, end)             # Step 1: Get data

data = MACD_Signal(data)                        # Step 2: Generate buy/sell signals
# Plot
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title('Price and MACD Indicator')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(data['MACD'], label='MACD', color='purple')
plt.plot(data['Signal'], label='Signal', color='orange')
plt.bar(data.index, data['Histogram'], label='Histogram', color='gray')
plt.legend()

plt.tight_layout()
plt.show()

current_MACD = data['MACD'].iloc[-1] - data['Signal'].iloc[-1]
if current_MACD > 0:
    print("\nMACD shows stock has bullish momentum")
elif current_MACD < 0:
    print("\nMACD shows stock has bearish momentum")
else:
    yesterday_MACD = data['MACD'].iloc[-2] - data['Signal'].iloc[-2]
    if yesterday_MACD < 0:
        print("\nMACD shows stock is starting an upward trend")
    else:
        print("\nMACD shows stock is starting a downward trend")

#Stochastic Oscillator
def Stochastic_Oscillator(data, fortnight=14, half_week = 3):
    data["Fortnight_High"] = data["Close"].rolling(fortnight).max()
    data["Fortnight_Low"] = data["Close"].rolling(fortnight).min()
    data["K%"] = (data["Close"] - data["Fortnight_Low"])/(data["Fortnight_High"] - data["Fortnight_Low"])
    data["%D"] = data["Close"].rolling(half_week).mean()
    return data

data = Stochastic_Oscillator(data)

current_SO = data["%D"].iloc[-1]
if current_SO < 0.2:
    print("\nStochastic Oscillator shows buy stock")
elif current_SO > 0.8:
    print("\nStochastic Oscillator shows sell stock")
else:
    print("\nStochastic Oscillator shows hold stock")
