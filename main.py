from typing import Optional
import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/api/getRandomSymbol")
async def get_random_symbol():
    # 預先定義5檔SP500股票
    sp500_stocks = [
        {"symbol": "AAPL", "company": "Apple Inc."},
        {"symbol": "MSFT", "company": "Microsoft Corporation"},
        {"symbol": "GOOGL", "company": "Alphabet Inc."},
        {"symbol": "AMZN", "company": "Amazon.com, Inc."},
        {"symbol": "TSLA", "company": "Tesla, Inc."}
    ]
    
    # 隨機選擇一檔股票
    random_stock = random.choice(sp500_stocks)
    
    return random_stock

