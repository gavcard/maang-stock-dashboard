import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine("postgresql://gavcard:@localhost:5432/maang_data")

st.title("📈 MAANG Stock Dashboard")

# Ticker options
tickers = ["meta", "aapl", "amzn", "nflx", "googl"]
ticker = st.selectbox("Choose a stock ticker:", tickers)

# Query the latest 100 rows
query = f'SELECT * FROM "{ticker}" ORDER BY "Date" DESC LIMIT 100'
df = pd.read_sql(query, engine)

# Display table
st.subheader(f"Latest Data for {ticker.upper()}")
st.dataframe(df)

# Line chart for stock price
st.subheader(f"{ticker.upper()} Closing Price Over Time")
st.line_chart(df.sort_values("Date")["Close"])

# Optional volume chart
if st.checkbox("Show volume chart"):
    st.subheader("Trading Volume")
    st.bar_chart(df.sort_values("Date")["Volume"])
