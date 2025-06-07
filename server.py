from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StockRequest(BaseModel):
    ticker: str

@app.post("/mcp")
async def get_stock_info(req: StockRequest):
    # Dummy prices; replace with real API or logic
    dummy_prices = {
        "AAPL": 175.25,
        "MSFT": 342.18,
        "GOOGL": 138.50
    }
    return {"price": dummy_prices.get(req.ticker, 100.0)}