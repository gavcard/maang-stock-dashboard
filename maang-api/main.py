from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI()

# Allow requests from anywhere (for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- Later restrict this to your Streamlit domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your Supabase PostgreSQL connection string
DB_URL = "postgresql://postgres:kendamam31Gummie%21@db.qasdnzgbmviflbgwnbla.supabase.co:5432/postgres"
engine = create_engine(DB_URL)

@app.get("/stocks/{ticker}")
def get_stock_data(ticker: str):
    try:
        # Query latest 100 rows from the stock table
        query = f'SELECT * FROM "{ticker.lower()}" ORDER BY "Date" DESC LIMIT 100'
        df = pd.read_sql(query, engine)
        return df.to_dict(orient="records")  # Return as JSON list of dicts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
