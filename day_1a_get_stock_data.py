import yfinance as yf
import pandas as pd

# Define the ticker and the time period
TICKER = 'AAPL'
START_DATE = '2023-11-01'
END_DATE = '2024-11-01'

print(f"Downloading stock data for {TICKER}...")

# Download stock data
stock_data = yf.download(TICKER, start=START_DATE, end=END_DATE)

# Save the data to a CSV file
stock_data.to_csv('stock_data.csv')

print(f"Successfully saved stock data to 'stock_data.csv'")
print(stock_data.head())