from typing import Optional
import random
import json
from pathlib import Path

from fastapi import FastAPI

app = FastAPI()


def load_sp500_data():
    """Load S&P 500 data from JSON file"""
    json_path = Path("data/sp500.json")
    with open(json_path, "r") as f:
        return json.load(f)


# 全域變數儲存 SP500 數據
SP500_DATA = load_sp500_data()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/getRandomSymbol")
async def get_random_symbol():
    """隨機返回一個 S&P 500 成分股的詳細信息"""
    # 從預加載的數據中隨機選擇一個股票
    random_stock = random.choice(SP500_DATA)
    return random_stock
