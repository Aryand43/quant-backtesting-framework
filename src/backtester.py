import yfinance as yf
import pandas as pd
import os
from joblib import Memory

# Caching fetched data to avoid redundant API calls
cache_dir = "../data"
os.makedirs(cache_dir, exist_ok=True)
memory = Memory(cache_dir, verbose=0)

@memory.cache
def fetch_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Fetch historical stock data using yfinance.
    Args:
        ticker (str): Stock ticker symbol.
        start (str): Start date in YYYY-MM-DD format.
        end (str): End date in YYYY-MM-DD format.
    Returns:
        pd.DataFrame: DataFrame containing the adjusted close price.
    """
    data = yf.download(ticker, start=start, end=end)
    data = pd.DataFrame(data["Adj Close"])
    data.rename(columns={"Adj Close": "price"}, inplace=True)
    return data

if __name__ == "__main__":
    # Example: Fetch data for AAPL
    ticker = "AAPL"
    start_date = "2022-01-01"
    end_date = "2023-01-01"
    data = fetch_data(ticker, start_date, end_date)
    print(data)
