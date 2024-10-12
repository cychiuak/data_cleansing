import sys
sys.path.append("/Users/andersonchiu/opt/anaconda3/lib/python3.12/site-packages")
import yfinance as yf
import pandas as pd

from datetime import datetime, timedelta

def get_stock_prices(symbol, date_str):
    """
    Fetch the opening and closing price of a stock on a given date.
    
    :param symbol: The stock ticker symbol (e.g., 'AAPL', 'GOOG').
    :param date_str: The date in 'YYYY-MM-DD' format.
    :return: A dictionary with the opening and closing price or an error message.
    """
    # Parse the input date string into a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Fetch one day of data with one day buffer on both sides to ensure we capture the date
    start_date = date - timedelta(days=1)
    end_date = date + timedelta(days=1)
    
    # Download the stock data for that range
    stock_data = yf.download(symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    
    # Ensure there is data for the requested date
    if date_str in stock_data.index.strftime('%Y-%m-%d'):
        # Extract the row corresponding to the requested date
        day_data = stock_data.loc[date_str]
        return {
            'date': date_str,
            'open': day_data['Open'],
            'close': day_data['Close'],
        }
    else:
        return {'error': f"No data available for {symbol} on {date_str}"}

# Example usage
symbol = 'AAPL'  # Apple stock symbol
date = '2023-10-06'  # Example date

prices = get_stock_prices(symbol, date)

if 'error' in prices:
    print(prices['error'])
else:
    print(f"Stock: {symbol}")
    print(f"Date: {prices['date']}")
    print(f"Opening Price: {prices['open']}")
    print(f"Closing Price: {prices['close']}")

# # Specify stock symbol, e.g., 'AAPL' for Apple
# stock_symbol = 'frsx'

# # Set the date range
# start_date = '2015-01-01'
# end_date = '2018-12-31'

# # Fetch data using yfinance
# stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# # Display the first few rows of the data
# print(stock_data.head())

# # Optionally, save the data to a CSV file
# stock_data.to_csv(f'{stock_symbol}_2015_to_2018.csv')

# # Display the last few rows to verify
# print(stock_data.tail())