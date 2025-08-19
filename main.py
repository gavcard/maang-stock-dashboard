import pandas as pd
from sqlalchemy import create_engine
import yfinance as yf

# PostgreSQL connection details
DB_USER = 'gavcard'
DB_PASS = ''
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'maang_data'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]

for ticker in tickers:
    print(f"Downloading live data for {ticker} from Yahoo Finance...")
    df = yf.download(ticker, start="2023-01-01")
    df.reset_index(inplace=True)
    # df.to_csv(f"{ticker}_stock_data.csv", index=False) -- export to csv


    # Flatten any tuple column names (take first element if tuple)
    df.columns = [col if isinstance(col, str) else col[0] for col in df.columns]

    print(f"Uploading {ticker} data into PostgreSQL...")
    df.to_sql(ticker.lower(), engine, if_exists='replace', index=False)
    print(f"Loaded {ticker} data successfully!")

print("All live data loaded into PostgreSQL!")
