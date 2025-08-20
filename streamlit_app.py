import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# --- Load DB credentials from secrets.toml ---
db = st.secrets["database"]

# --- Create DB connection URL ---
db_url = f"postgresql://{db.user}:{db.password}@{db.host}:{db.port}/{db.dbname}"
engine = create_engine(db_url)

# --- Whitelisted tickers to avoid SQL injection ---
VALID_TICKERS = ["aapl", "msft", "goog", "amzn", "meta"]

# --- UI ---
st.title("📈 MAANG Stock Dashboard")
ticker = st.selectbox("Select a stock ticker:", VALID_TICKERS)

# --- Fetch data ---
try:
    query = f'SELECT * FROM "{ticker}" ORDER BY "Date" DESC LIMIT 100'
    df = pd.read_sql(query, engine)

    st.subheader(f"Latest 100 entries for {ticker.upper()}")
    st.dataframe(df)

except Exception as e:
    st.error(f"Error loading data: {e}")
