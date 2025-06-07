import pandas as pd
import asyncio
from fastmcp import Client
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List, Dict, Any


class GraphState(TypedDict, total=False):
    client: Client
    portfolio: List[dict]
    market: Dict[str, Any]


def load_portfolio(state: GraphState) -> GraphState:
    df = pd.read_csv("portfolio.csv")
    return {"portfolio": df.to_dict(orient="records")}


async def fetch_market(state: GraphState) -> GraphState:
    client = state["client"]
    tickers = [row["Ticker"] for row in state["portfolio"]]
    quotes = {}
    for ticker in tickers:
        try:
            result = await client.call_tool("get_stock_info", {"ticker": ticker})
            if isinstance(result, dict) and "price" in result:
                quotes[ticker] = {"price": result["price"]}
            elif isinstance(result, dict):
                quotes[ticker] = {"error": result}
            elif isinstance(result, list):
                quotes[ticker] = {"raw": result}
            else:
                quotes[ticker] = {"error": "Unknown response format"}
        except Exception as e:
            quotes[ticker] = {"error": str(e)}
    return {"market": quotes}


async def main():
    builder = StateGraph(GraphState)
    builder.add_node("LoadPortfolio", load_portfolio)
    builder.add_node("FetchMarket", fetch_market)
    builder.add_edge(START, "LoadPortfolio")
    builder.add_edge("LoadPortfolio", "FetchMarket")
    builder.add_edge("FetchMarket", END)
    graph = builder.compile()

    async with Client("http://localhost:8000/sse") as client:
        if hasattr(client, "connect") and not client.connected:
            await client.connect()
        result = await graph.ainvoke({"client": client})

    print("\n🏦 Market snapshot")
    total_value = 0.0
    for row in result["portfolio"]:
        ticker = row["Ticker"]
        shares = row["Shares"]
        data = result["market"].get(ticker, {})
        if "price" in data:
            price = data["price"]
            print(f"  {ticker:10} : {price}")
            total_value += price * shares
        elif "error" in data:
            print(f"  {ticker:10} : ERR ({data['error'][:50]})")
        elif "raw" in data:
            print(f"  {ticker:10} : raw: {data['raw']}")
        else:
            print(f"  {ticker:10} : unknown")

    print(f"\nTotal Portfolio Value: ${total_value:,.2f}")


if __name__ == "__main__":
    asyncio.run(main())