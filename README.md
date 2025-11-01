# MACD-Stochastic-Oscillator

This script creates the two technical indicators, MACD and Stochastic Oscillators, to determine whether a stock is currently a buy, sell or hold based on its recent momentum

---

## 🧩 Features
- Fetches stock price data from Yahoo Finance.
- Calculates MACD and signal lines.
- Then plots these to determine the stock's current momentum.
- Calculates the Stochastic Oscillator, then determines whether the stock should be buy/sell/hold.

---

## 📖 Some Theory
Moving-Average Convergence/Divergence and Stochastic Oscillators are technical indicators that you use to determine whether now is a good time to buy/sell.

Technical indicators are often used for day trading, but unfortunately these are not an exact science.

The MACD represents the difference between the short term average and the long term average and it measures momentum. If it is greater than 0 than there is bullish momentum in the stock, whereas if it is less than 0 then there is bearish momentum.

While the signal is the average of the MACD, and it is like a "trigger", it indicates whether bullish momentum is slowing down or speeding up (speeding up if MACD is above the signal), and same for bearish momentum.

The stochastic oscillator indicates whether a stock should be bought, sold or held.

It starts with the %K calculation, which is just the current closing price minus the lowest closing price in a recent short term window (the code just uses 14 days), all divided by the hughest closing price in a recent short term window minus the lowest closing price in a recent short term window.

Then there is the %D calculation which is just a 3-day moving average of the %K calculation.

This %D calculation then indicates whether you should buy/sell/hold, and the below are the conditions for each:
- %D <= 20%: Stock is oversold, so buy
- %D >= 80%: Stock is overbought, so sell
- %D is inbetween the above range: stock is neither overbought nor oversold, so just hold

---

## 📈 Outcome
We can use these technical indicators to day trade, or instead, just use this complementary to your fundamental analysis, which helps determine good stocks to buy/sell, and then these technical indicators simply help with timing, in when to buy/sell the stocks you discovered through your technical analysis.

---

## 📑 Sources
CFA Curriculum - Level 1

---

## ⚙️ Requirements
Install dependencies:
```bash
pip install numpy pandas yfinance matplotlib 
