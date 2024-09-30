import sys
sys.path.append("/Users/andersonchiu/opt/anaconda3/lib/python3.12/site-packages")
import yfinance as yf
import pandas as pd

# Specify stock symbol, e.g., 'AAPL' for Apple
stock_symbol = 'frsx'

# Set the date range
start_date = '2015-01-01'
end_date = '2018-12-31'

# Fetch data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display the first few rows of the data
print(stock_data.head())

# Optionally, save the data to a CSV file
stock_data.to_csv(f'{stock_symbol}_2015_to_2018.csv')

# Display the last few rows to verify
print(stock_data.tail())