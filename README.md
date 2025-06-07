# Financial Reasoning Agent Demo

## Overview
This repository demonstrates a financial reasoning agent built with LangGraph. The agent loads a portfolio, queries a Model Context Protocol (MCP) for live market data, summarizes the portfolio's value, and answers complex financial queries based on the portfolio, news, and market trends.

## Project Structure

```
financial-agent-demo/
├── README.md
├── agent.py
├── portfolio.csv
└── finance_mcp/
    ├── requirements.txt
    └── server.py
```

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd financial-agent-demo
```

### Step 2: Setup Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r finance_mcp/requirements.txt
pip install langgraph pandas fastmcp
```

### Step 3: Start the MCP Server
```bash
cd finance_mcp
uvicorn server:app --port 8000
```

### Step 4: Run the Agent
```bash
python agent.py
```

## Sample Portfolio (`portfolio.csv`)

```csv
Ticker,Shares
AAPL,10
MSFT,5
GOOGL,8
```

## Example Queries & Outputs

### 🔹 Simple Query
```bash
$ python agent.py

🏦 Market Snapshot:
  AAPL     : 175.25
  MSFT     : 342.18
  GOOGL    : 138.50

Total Portfolio Value: $4,385.40
```

---

### 🔸 Complex Query Examples

#### ❓ Query:
> Given recent news and current market trends, should I increase my holdings in AAPL?

**✅ Agent's Answer:**
> Based on the recent news highlighting strong earnings reports and positive market trends, increasing your holdings in AAPL could be favorable. The stock has shown consistent growth, and analysts forecast continued performance improvement. Consider your risk tolerance before making changes.

---

#### ❓ Query:
> How does the current economic news affect my technology-focused portfolio?

**✅ Agent's Answer:**
> The current economic news indicates a positive outlook for technology companies due to increasing demand in cloud computing, AI innovations, and robust earnings reports from major tech firms. Your technology-focused portfolio, including AAPL, MSFT, and GOOGL, is likely positioned well to benefit from these trends.

---

#### ❓ Query:
> Which of my holdings are underperforming based on the past month’s trend?

**✅ Agent's Answer:**
> Among your holdings, GOOGL has shown the least price appreciation over the past month compared to AAPL and MSFT. While it’s still performing steadily, it lags slightly behind the sector average. You may want to watch news sentiment or quarterly earnings updates before adjusting.

---

## 📊 Slides

Slides explaining the overall approach and workflow can be found under:

```
slides/Financial_Agent_Demo_Slides.pptx
```
