import yfinance as yf
import pandas as pd
import ta
import os

print("Fetching Stock Data...")

stock_symbol = "RELIANCE.NS"

data = yf.download(stock_symbol, start="2015-01-01", end="2024-12-31")


if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.droplevel(1)


data["SMA_20"] = ta.trend.sma_indicator(data["Close"], window=20)
data["EMA_20"] = ta.trend.ema_indicator(data["Close"], window=20)
data["RSI"] = ta.momentum.rsi(data["Close"], window=14)
data["MACD"] = ta.trend.macd(data["Close"])
data["Bollinger_High"] = ta.volatility.bollinger_hband(data["Close"])
data["Bollinger_Low"] = ta.volatility.bollinger_lband(data["Close"])


data = data.dropna()

print(data.tail())


os.makedirs("data", exist_ok=True)

data.to_csv("data/reliance_stock_with_indicators.csv")

print("Indicators added and data saved!")