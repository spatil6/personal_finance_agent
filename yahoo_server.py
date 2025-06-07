from fastapi import FastAPI
from pydantic import BaseModel
import yfinance as yf

app = FastAPI()

class StockRequest(BaseModel):
    ticker: str

@app.post("/mcp")
async def get_stock_info(req: StockRequest):
    try:
        stock = yf.Ticker(req.ticker)
        price = stock.info.get("regularMarketPrice")
        if price is None:
            return {"error": f"Price not found for {req.ticker}"}
        return {"price": price}
    except Exception as e:
        return {"error": str(e)}