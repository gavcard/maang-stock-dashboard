import pandas as pd
from sqlalchemy import create_engine
import yfinance as yf

# Supabase PostgreSQL connection details
DB_USER = 'postgres'
DB_PASS = 'kendamam31Gummie!'
DB_HOST = 'db.qasdnzgbmviflbgwnbla.supabase.co'
DB_PORT = '5432'
DB_NAME = 'postgres'

# Create SQLAlchemy engine
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# MAANG tickers
tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]

for ticker in tickers:
    print(f"📥 Downloading data for {ticker} from Yahoo Finance...")
    df = yf.download(ticker, start="2023-01-01")
    df.reset_index(inplace=True)

    # Ensure clean column names
    df.columns = [col if isinstance(col, str) else col[0] for col in df.columns]

    print(f"Uploading {ticker} data into Supabase PostgreSQL...")
    df.to_sql(ticker.lower(), engine, if_exists='replace', index=False)
    print(f"{ticker} data uploaded successfully!")

print("🚀 All MAANG stock data loaded into Supabase!")
