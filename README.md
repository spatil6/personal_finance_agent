# personal_finance_agent
Financial Reasoning Agent Demo

Overview

This repository demonstrates a financial reasoning agent built with LangGraph. The agent loads a portfolio, queries a Model Context Protocol (MCP) for live market data, summarizes the portfolio's value, and answers complex financial queries based on the portfolio, news, and market trends.

Project Structure

financial-agent-demo/
├── README.md
├── agent.py
├── portfolio.csv
└── finance_mcp/
    ├── requirements.txt
    └── server.py

Setup Instructions

Step 1: Clone the Repository

git clone <repository-url>
cd financial-agent-demo

Step 2: Setup Virtual Environment

python -m venv .venv
source .venv/bin/activate
pip install -r finance_mcp/requirements.txt
pip install langgraph pandas fastmcp

Step 3: Start the MCP Server

cd finance_mcp
uvicorn server:app --port 8000

Step 4: Run the Agent

python agent.py

Sample Portfolio (portfolio.csv)

Ticker,Shares
AAPL,10
MSFT,5
GOOGL,8

Example Queries & Outputs

Simple Query

$ python agent.py

🏦 Market Snapshot:
  AAPL     : 175.25
  MSFT     : 342.18
  GOOGL    : 138.50

Total Portfolio Value: $4,385.40

Complex Query Examples

Query:

Given recent news and current market trends, should I increase my holdings in AAPL?

Agent's Answer:

Based on recent news highlighting strong earnings reports and positive market trends, increasing your holdings in AAPL could be favorable. The stock has shown consistent growth, and analysts forecast continued performance improvement. However, consider your risk tolerance and overall portfolio strategy before making any adjustments.

Query:

How does the current economic news affect my technology-focused portfolio?

Agent's Answer:

The current economic news indicates a positive outlook for technology companies due to increasing demand in cloud computing, AI innovations, and robust earnings reports from major tech firms. Your technology-focused portfolio, including AAPL, MSFT, and GOOGL, is likely positioned well to benefit from these trends.

Query:

Should I diversify my portfolio beyond technology given current market volatility?

Agent's Answer:

Considering current market volatility, diversifying your portfolio beyond technology could reduce risk exposure. Allocating a portion of your investments to sectors like healthcare, utilities, or consumer staples may provide stability and balance your portfolio against tech-specific downturns.

Slides

Slides explaining the overall approach and workflow can be found under slides/Financial_Agent_Demo_Slides.pptx.
